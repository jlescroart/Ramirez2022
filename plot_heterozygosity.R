#### Description: Plot local heterozygosity estimates from ANGSD as per-sample boxplots.
#### Written by: Henrique V. Figueiró - henriquevf@gmail.com as neofelis_het_plot.R
#### Adapted by Jonas Lescroart on 03 April 2021.

# Libraries
library(ggplot2)

# Read input
het_tbl <- read.table("leopardus_selection_heterozygosity_autosomal_18MAY21.txt", header = F)
colnames(het_tbl) <- c("Heterozygosity", "Sample")

# Create boxplot
ggplot(het_tbl, aes(x=Sample, y=Heterozygosity)) + geom_boxplot(outlier.shape=NA) +
  ylab("Autosomal heterozygosity\n") + xlab("\nSample") + theme_minimal() +
  scale_y_continuous(breaks = seq(0,0.01,by=0.0005), limits = c(0.0,0.0045)) +
  scale_x_discrete(limits = c("Ltigrinus","Lcolocola","Lgeoffroyi","Lwiedii","Lpardalis2","Lpardalis6","Pbengalensis","Pconcolor","Hyagouaroundi","Ccaracal","Ppardus")) +
  theme(axis.text.x=element_text(angle = 90, vjust = 0.6, size = 12))

# To summarize statistics for a given sample
summary(het_tbl$Heterozygosity[het_tbl$Sample=="Lwiedii"])
