from ..fileProcessor import FileProcessor
from ...types.readerType import ReaderType
from ...types.infileType import InfileType
from ...metadata_infile.edge.inMetaEdgeStitch import InMetaEdgeStitch


class EdgeStitchProcessor(FileProcessor):
    IN_META_CLASS = InMetaEdgeStitch

    def __init__(self):
        self.use_cols = self.IN_META_CLASS.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_EDGE_STITCH,
                         infileType=InfileType.IN_EDGE_STITCH, mapping_sep=self.IN_META_CLASS.MAPPING_SEP)


    def individual_postprocessing(self, data):
        data = data[data.chemID.str.startswith('CIDs')]
        self.stitch_to_pubchem_id(data,self.use_cols.index('chemID'))
        return data