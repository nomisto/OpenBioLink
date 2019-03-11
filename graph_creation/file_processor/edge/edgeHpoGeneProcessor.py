from graph_creation.file_processor.fileProcessor import FileProcessor
from graph_creation.Types.readerType import ReaderType
from graph_creation.Types.infileType import InfileType
from graph_creation.metadata_infile.edge.inMetaEdgeHpoGene import InMetaEdgeHpoGene


class EdgeHpoGeneProcessor(FileProcessor):
    IN_META_CLASS = InMetaEdgeHpoGene

    def __init__(self):
        self.use_cols = self.IN_META_CLASS.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_EDGE_HPO_GENE,
                         infileType=InfileType.IN_EDGE_HPO_GENE, mapping_sep=self.IN_META_CLASS.MAPPING_SEP)