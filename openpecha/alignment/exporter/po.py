import re
from pathlib import Path

import polib
from botok.tokenizers.sentencetokenizer import get_normalized_sentence
from botok.tokenizers.wordtokenizer import WordTokenizer

from openpecha.alignment.exporter import Exporter


class PoExporter(Exporter):
    def __init__(self, alignment_path) -> None:
        super().__init__(alignment_path)
        self.file = polib.POFile()
        self.file.metadata = {
            "MIME-Version": "1.0",
            "Content-Type": "text/plain; charset=utf-8",
            "Content-Transfer-Encoding": "8bit",
        }

    def _create_entry(
        self, msgid, msgstr="", msgctxt=None, comment=None, tcomment=None
    ):
        """

        :param msgid: string, the entry msgid.
        :param msgstr: string, the entry msgstr.
        :param msgctxt: string, the entry context.
        :param comment: string, the entry comment.
        :param tcomment: string, the entry translator comment.
        """
        entry = polib.POEntry(
            msgid=msgid,
            msgstr=msgstr,
            msgctxt=msgctxt,
            comment=comment,
            tcomment=tcomment,
        )
        self.file.append(entry)

    def write_to_file(self, filename):
        self.file.save(filename)

    def segment_to_entries(self, pecha_id, pecha_path, lang):
        segments = self.get_segment_texts(pecha_id, pecha_path)
        wt = WordTokenizer()
        for pair_id, segment_text in segments.items():
            segment_text = segment_text.replace("\n", "")
            if lang == "bo":
                segment_tokens = wt.tokenize(segment_text, split_affixes=True)
                tokenized_segment = get_normalized_sentence(segment_tokens)
                self._create_entry(
                    msgid=tokenized_segment, msgctxt=pair_id, tcomment=segment_text
                )
            else:
                self._create_entry(msgid=segment_text, msgctxt=pair_id)

    def export(self, output_dir):
        segment_srcs = self.alignment.get("segment_sources", {})
        for seg_src_id, seg_src in segment_srcs.items():
            lang = seg_src.get("lang", "")
            if lang:
                self.segment_to_entries(seg_src_id, src_path=None, lang=lang)
                self.write_to_file((Path(output_dir) / f"{lang}.po"))
            self.file = polib.POFile()
            self.file.metadata = {
                "MIME-Version": "1.0",
                "Content-Type": "text/plain; charset=utf-8",
                "Content-Transfer-Encoding": "8bit",
            }
