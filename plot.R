library(ggplot2)
ggplot(opto_plot, aes(x = exp_time/60/60, y = FP2_emit1, colour = 'mScarlet')) + 
  geom_line() +
  geom_vline(xintercept = 4) +
  geom_vline(xintercept = 8) +
  geom_vline(xintercept = 12) +
  geom_vline(xintercept = 16) +
  geom_vline(xintercept = 20)

ggplot(opto_plot, aes(x = exp_time/60/60)) + 
  geom_rect(aes(xmin = 4, xmax = 8, ymin = -Inf, ymax = +Inf), 
          fill = "blue", alpha = 0.5) +
  geom_rect(aes(xmin = 12, xmax = 16, ymin = -Inf, ymax = +Inf), 
            fill = "blue", alpha = 0.5) +
  geom_line(aes(y = opto_plot$FP2_emit1, colour = 'mScarlet')) +
  theme_bw() +
  labs(x = 'Time, hours',
       y = 'mScarlet',
       title = 'Optogenetic Control of mScarlet Production') +
  geom_smooth(aes(y = opto_plot$FP2_emit1))


#####get loess
library(mgcv)
smooth_fp <- predict(gam(FP2_emit1 ~ s(exp_time), data = opto_plot))
smooth_fp
opto_plot$fp_gam <- smooth_fp

####plot w that only

ggplot(opto_plot, aes(x = exp_time/60/60)) + 
  geom_rect(aes(xmin = 4, xmax = 8, ymin = -Inf, ymax = +Inf), 
            fill = "blue", alpha = 0.5) +
  geom_rect(aes(xmin = 12, xmax = 16, ymin = -Inf, ymax = +Inf), 
            fill = "blue", alpha = 0.5) +
  geom_line(aes(y = opto_plot$fp_gam, colour = 'mScarlet')) +
  theme_bw() +
  labs(x = 'Time, hours',
       y = 'mScarlet',
       title = 'Optogenetic Control of mScarlet Production')

##looks good export new

write.csv(opto_plot, file = 'opto_gam.csv', row.names = FALSE)
