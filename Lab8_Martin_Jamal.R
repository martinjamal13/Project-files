
#ttest
Reg = c(16,20,21,22,23,22,27,25,27,28)
Premium = c(19,22,24,24,25,25,26,26,28,32)
t.test(Reg,Premium,pooled=F,paired=T)
 
#load file check stas
supers = read.csv(file.choose())
summarytools::descr(supers$Worldwide)
sd(supers$Worldwide[supers$Studio == "DC"])
summarytools::descr(supers$Worldwide[supers$Studio == "DC"])

#ttest
t.test(supers$Worldwide[supers$Studio == "DC"],supers$Worldwide[supers$Studio == "Marvel"], pooled = T, paired = F, conf.level = 0.90)
 
#cohenD
install.packages("lsr")
library(lsr)
cohensD(supers$Worldwide[supers$Studio == "DC"],supers$Worldwide[supers$Studio == "Marvel"])

#filtering based on year and studio/test
dis_before = supers$Review[supers$Year <= 2009 & supers$Studio == "Marvel"]
dis_after = supers$Review[supers$Year > 2009 & supers$Studio == "Marvel"]
summarytools:: descr(dis_before)
summarytools:: descr(dis_after)
summarytools::descr(supers$Review[supers$Studio == "Marvel"])
t.test(dis_after,dis_before, pooled =T, paired = F, conf.level = .90)
cohensD(dis_after,dis_before)
library("pwr")
plot(pwr.t.test(power = NULL, n =63, sig.level = 0.05, type= "two.sample", alt = "two.sided", d = .5))

