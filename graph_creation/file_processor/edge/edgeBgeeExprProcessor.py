from graph_creation.file_processor.fileProcessor import FileProcessor
from graph_creation.Types.readerType import ReaderType
from graph_creation.Types.infileType import InfileType
from graph_creation.metadata_infile.edge.inMetaEdgeBgeeExpr import InMetaEdgeBgeeExpr


class EdgeBgeeExprProcessor(FileProcessor):
    IN_META_CLASS = InMetaEdgeBgeeExpr

    def __init__(self):
        self.use_cols =   self.IN_META_CLASS.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_EDGE_BGEE,
                         infileType=InfileType.IN_EDGE_BGEE_EXPR, mapping_sep= self.IN_META_CLASS.MAPPING_SEP)

    def individual_preprocessing(self, data):
        data = data[data.expression == 'present']
        return data