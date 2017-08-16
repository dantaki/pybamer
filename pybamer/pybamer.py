#!/usr/env python
import pysam 
import os,argparse,sys
from argparse import RawTextHelpFormatter
from tqdm import tqdm
from collections import OrderedDict
import numpy as np
class Arguments():
	def __init__(self):
		splash='pybamer        --coverage and read length statistics from your bam file--\n'
		parser = argparse.ArgumentParser(description=splash,formatter_class=RawTextHelpFormatter)
		reqArgs = parser.add_argument_group('required arguments')
		optArgs = parser.add_argument_group('Optional arguments')
		reqArgs.add_argument('-i', help='BAM file',required=True,type=str)
		optArgs.add_argument('-q', help='Mapping Quality cutoff [10]',required=False,type=int,default=10)
		optArgs.add_argument('-o',help='Output [pybamer.out]',required=False,type=str,default='pybamer.out')
		args = parser.parse_args()
		self.ifh = args.i
		self.q = args.q
		self.ofh = args.o
class Bam():
	def __init__(self,ifh):
		self.ifh=ifh
		self.bam=pysam.AlignmentFile(ifh,'rb')
		self.ref=OrderedDict()
		self.reads={}
		for x,y in zip(self.bam.references, self.bam.lengths): 
			self.reads[x]={}
			self.ref[x]=float(y)
	def computeStats(self,Q,ofh):
		for al in tqdm(self.bam.fetch(until_eof=True)):
			if (	al.cigartuples == None 
				or al.is_unmapped 
				or al.mapping_quality < Q 
				or al.reference_length==0 
				or al.reference_length==None
			   ): 
				continue
			if self.reads[al.reference_name].get(al.query_name)==None:
				self.reads[al.reference_name][al.query_name]=al.reference_length
			else:   self.reads[al.reference_name][al.query_name]+=al.reference_length
		o = open(ofh,'w')
		o.write('#REF\tCOVERAGE\tAVG_READ_LEN\tN_READS\tREF_LEN\n')
		gL,gN,gA=0,0,[] 
		for ref,leng in self.ref.items():
			gL+=leng
			N=len(self.reads[ref])
			gN+=N
			gA.extend(list(self.reads[ref].values()))
			avg=0
			if N>0:avg=np.mean(self.reads[ref].values())
			o.write('\t'.join(map(str,(ref,(avg*N)/leng,avg,N,int(leng))))+'\n')
		if len(gA)>0:gA = np.mean(gA)
		else: gA=0
		o.write('\t'.join(map(str,('GENOME',(gA*gN)/gL,gA,gN,int(gL))))+'\n')
		o.close()
def main(): 
	Args = Arguments()
	bam = Bam(Args.ifh)
	bam.computeStats(Args.q,Args.ofh)		
