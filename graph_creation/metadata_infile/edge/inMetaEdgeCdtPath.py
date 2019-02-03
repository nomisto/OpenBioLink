from edgeType import EdgeType
from graph_creation.Types.infileType import InfileType
from graph_creation.metadata_infile.infileMetadata import InfileMetadata
from nodeType import NodeType


class InMetaEdgeCdtPath(InfileMetadata):
    CSV_NAME = "DB_CDT_gene_pathway.csv"
    USE_COLS = ['geneID', 'pathID']
    NODE1_COL = 0
    NODE2_COL = 1
    QSCORE_COL = None
    NODE1_TYPE = NodeType.GENE
    NODE2_TYPE = NodeType.PATHWAY
    EDGE_TYPE = EdgeType.GENE_PATHWAY
    INFILE_TYPE = InfileType.IN_EDGE_CDT_PATH
    MAPPING_SEP = None

    def __init__(self, folder_path):
        super().__init__(csv_name=InMetaEdgeCdtPath.CSV_NAME,
                         folder_path=folder_path,
                         infileType=InMetaEdgeCdtPath.INFILE_TYPE)