#!/bin/bash
data_dir="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
echo Data_dir:  $data_dir
data_file=pacbio_filtered.fastq
sample_data_dir=selfSampleData

if [ -f $data_file* ]; then
    echo $data_file "exists; Exiting"
else
    if [ -f $sample_data_dir/$data_file ]; then
	echo $data_file "exists in " $sample_data_dir "; Linking"
	ln -s $sample_data_dir/$data_file .
    else
	echo $data_file "DOES NOT exist; Downloading"
	wget -O- http://www.cbcb.umd.edu/software/PBcR/data/selfSampleData.tar.gz | tar zxf -
	ln -s $sample_data_dir/$data_file .
    fi
fi


