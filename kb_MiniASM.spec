/*
A KBase module: kb_MiniASM
A simple wrapper for MiniASM Assembler
https://github.com/lh3/miniasm
*/

module kb_MiniASM {

    /* The workspace object name of a PairedEndLibrary file, whether of the
       KBaseAssembly or KBaseFile type.
    */
    typedef string single_end_lib;
    typedef int    bool;

    /* Input parameters for running MiniASM.
        string workspace_name - the name of the workspace from which to take
           input and store output.
        list<paired_end_lib> read_libraries - Illumina PairedEndLibrary files
            to assemble.
        string output_contigset_name - the name of the output contigset
    */
    typedef structure {
        bool    prefilter;
        int     min_match_len;   /* default 100 */
        float   min_identity;    /* default 0.05 */
        int     min_span;        /* default 2000 */
        int     min_coverage;    /* default 3 */
    } preSelect_args_type;

    typedef structure {
        int min_overlap;        /* default 2000 */
        int max_overhang_len;   /* default 1000 */
        int min_match_ratio;    /* default 0.8  */
    } overlap_args_type;

    typedef structure {
        int max_gap_diff;             /* default 1000 */
        int max_dist_bubble_pop;      /* default 3 */
        int small_unitig_threshold;   /* default 2000 */
        int rounds_short_overlap_rem; /* default 3 */
        float max_overlap_ratio;      /* 0.7  */
        float min_overlap_ratio;      /* 0.5  */
        float aggr_overlap_ratio;     /* 0.8  */
    } layout_args_type;

    typedef structure {
        string  output_info;       /* default ug */
        bool both_dir_arc;
        bool skip_1_pass;
        bool skip_2_pass;
        bool print_version;
    } misc_args_type;

    typedef structure {
        string               workspace_name;
        list<single_end_lib> read_libraries;                /*  input reads  */
        string               output_contigset_name;         /*  name of output contigs */
        int                  min_contig;                    /*  (=200) minimum size of contig */
        preSelect_args_type  preSelect_args;
        overlap_args_type    overlap_args;
        layout_args_type     layout_args;
        misc_args_type       misc_args;
    } MiniASM_Params;
    
    /* Output parameters for MiniASM run.
        string report_name - the name of the KBaseReport.Report workspace
            object.
        string report_ref - the workspace reference of the report.
    */
    typedef structure {
        string report_name;
        string report_ref;
    } MiniASM_Output;
    
    /* Run MiniASM on paired end libraries */
    funcdef run_MiniASM(MiniASM_Params params) returns(MiniASM_Output output)
        authentication required;
};
