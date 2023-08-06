from hexdump import hexdump

from . import ElfHeaderEditor
from .. import api, SECTION, EDITOR
from ..core import Editor
from ..elements.section_header import SectionHeader, SectionHeaderTable


class SectionHeaderEditor(Editor, api.SectionHeaderEditor):
    def read_section_header_table(self, rev_idx: int = -1) -> SectionHeaderTable:
        elfhdr_editor: ElfHeaderEditor = self.elf.get_editor(EDITOR.ELF_HEADER)
        elfhdr = elfhdr_editor.read_elf_header(rev_idx=rev_idx)
        rev = self.elf.revisions[rev_idx]
        cache = self.elf.get_cache(rev, 'sht')

        if sht := cache.lookup():
            return sht

        with open(rev, 'rb') as f:
            f.seek(elfhdr.shoff)
            sht_bytes = f.read(elfhdr.shnum * elfhdr.shentsize)

        assert elfhdr.shentsize == SectionHeader.size(self.elf)

        sht = SectionHeaderTable()

        for i in range(elfhdr.shnum):
            sh = SectionHeader.from_bytes(self.elf, sht_bytes[i*elfhdr.shentsize:(i+1)*elfhdr.shentsize])
            sht.append(sh)

        cache.update(sht)

        return sht

    def read_section_header(self, section: SECTION, rev_idx: int = -1) -> SectionHeader:
        for sh in self.read_section_header_table(rev_idx=rev_idx):
            if sh.name == str(section):
                return sh

    def __get_section_header_offset_by_name(self, section: SECTION):
        elfhdr_editor: ElfHeaderEditor = self.elf.get_editor(EDITOR.ELF_HEADER)
        elfhdr = elfhdr_editor.read_elf_header()

        with open(self.elf.get_current_revision(), 'rb') as f:
            f.seek(elfhdr.shoff)
            sht_bytes = f.read(elfhdr.shnum * elfhdr.shentsize)

        assert elfhdr.shentsize == SectionHeader.size(self.elf)

        offset = -1
        for i in range(elfhdr.shnum):
            sh = SectionHeader.from_bytes(self.elf, sht_bytes[i*elfhdr.shentsize:(i+1)*elfhdr.shentsize])
            if sh.name == str(section):
                offset = elfhdr.shoff + i * elfhdr.shentsize
                break

        return offset

    def write_section_header_table(self, sht: SectionHeaderTable):
        elfhdr_editor: ElfHeaderEditor = self.elf.get_editor(EDITOR.ELF_HEADER)
        elfhdr = elfhdr_editor.read_elf_header()
        rev = self.elf.get_current_revision()
        cache = self.elf.get_cache(rev, 'sht')

        with open(rev, 'r+b') as f:
            f.seek(elfhdr.shoff)
            for sh in sht:
                f.write(sh.to_bytes(self.elf))

        elfhdr.shnum = len(sht)

        elfhdr_editor.write_elf_header(elfhdr)

        cache.invalidate()

    def write_section_header(self, section: SECTION, sh: SectionHeader):
        offset = self.__get_section_header_offset_by_name(section)
        rev = self.elf.get_current_revision()
        cache = self.elf.get_cache(rev, 'sht')

        if offset < 0:
            raise ValueError

        with open(rev, 'r+b') as f:
            f.seek(offset)
            f.write(sh.to_bytes(self.elf))

        cache.invalidate()
