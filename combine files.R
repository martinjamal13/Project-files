library(readxl)
combine_info = read_xlsx(file.choose())
#check dat
str(combine_info)
#summary stats
install.packages("summarytools")
library(summarytools)
summarytools::descr(combine_info$`Arm Length (in)`)
summarytools::descr((combine_info$`Bench Press`))
descr(combine_info$`Height (in)`)
descr(combine_info$`Weight (lbs)`)
descr(combine_info$`40 Yard`)

#Correlation test to get a feel for relationship between variables
cor.test(combine_info$`40 Yard`,combine_info$`Arm Length (in)`)
cor.test(combine_info$`40 Yard`,combine_info$`Weight (lbs)`)
cor.test(combine_info$`40 Yard`,combine_info$`Height (in)`)
cor.test(combine_info$`40 Yard`,combine_info$`Bench Press`)

#cor.test(combine_info$BenchPress2, combine_info$ArmLength2)
#Regression test
reg_test = lm(combine_info$`40 Yard` ~ combine_info$`Arm Length (in)`+ combine_info$`Height (in)`+combine_info$`Weight (lbs)`+combine_info$`Bench Press`)
summary(reg_test)

#vif check
vif(reg_test)

#regression with imputation yielded the same results. Possible errors so did not use
#summary(lm(combine_info$BenchPress2~combine_info$ArmLength2))
#Violation test
plot(reg_test)

#scatterplot
plot(combine_info$`Arm Length (in)`, combine_info$`Bench Press`, main = "Arm Length vs Bench press", xlab = "Arm length", ylab = "Bench Press reps", cex.axis = 1.5, cex.lab = 1.5)
abline(reg_test, lwd = 2, col = "green")

#stargazer
install.packages("stargazer")
library(stargazer)
stargazer(reg_test, type = "text", title = "40 yard dash", digits = 1, flip = TRUE)

