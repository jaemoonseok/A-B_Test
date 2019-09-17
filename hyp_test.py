import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd
rottweiler_tl=fetchmaker.get_tail_length("rottweiler")
print(rottweiler_tl)
print(np.mean(rottweiler_tl), np.std(rottweiler_tl))

whippet_rescue=fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets=np.size(whippet_rescue)

pval= binom_test(num_whippet_rescues, num_whippets, p=0.08)

whip=fetchmaker.get_weight("whippet")
terr=fetchmaker.get_weight("terrier")
pitb=fetchmaker.get_weight("pitbull")

values = np.concatenate([whip, terr, pitb])
labels = ["whippet"] * len(whip) + ["terrier"] * len(terr) + ["pitbull"] * len(pitb)
print( pairwise_tukeyhsd(values, labels, 0.05))

whip_terr_pitb = f_oneway(whip, terr, pitb)
print(whip_terr_pitb)
whip_terr = pairwise_tukeyhsd(whip, terr)
whip_pitb = pairwise_tukeyhsd(whip, pitb)
terr_pitb = pairwise_tukeyhsd(terr, pitb)

poodle_colors= fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

color_table = [
  [ np.count_nonzero(poodle_colors=="black"),
    np.count_nonzero(shihtzu_colors== "black")],
  [np.count_nonzero(poodle_colors=="brown"),
    np.count_nonzero(shihtzu_colors== "brown")],
  [np.count_nonzero(poodle_colors=="gold"),
    np.count_nonzero(shihtzu_colors== "gold")],
  [np.count_nonzero(poodle_colors=="grey"),
    np.count_nonzero(shihtzu_colors== "grey")],
  [np.count_nonzero(poodle_colors=="white"),
    np.count_nonzero(shihtzu_colors== "white")]
]
print color_table

_, color_pval, _ ,_ = chi2_contingency(color_table)
print(color_pval)
