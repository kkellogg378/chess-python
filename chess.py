import tkinter as tk
from base64 import b64decode
from functools import partial

# Flags
debug_mode = True
isSelected = False
enPassant = False

# References
white = "White"
black = "Black"
selected_i = 8 # 8 means none selected
selected_j = 8
whosTurn = white
enPassant_j = 8

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Chess Python")
window['padx'] = 10
window['pady'] = 10

# Image references
empty = tk.PhotoImage(width = 1, height = 1)
empty_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAC9JREFUWEft0EERAAAMwjDwL3qTwSdV0EtzuQyrAQIECBAgQIAAAQIECBAgQGAt8IXeP+HAVxIZAAAAAElFTkSuQmCC"))

whitePawn         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAr5JREFUWEeNV23a4yAI1Gts7JHavWv7nmibvNdwH0AU+dD0T9NEcRhmIM3p5ienlGpbK6/hlv49Qtpd3t4grEDmnpBTTrWDQhQApg6gdEMgd260bT5mS46HhEPUBRMezRTLAGDQ8M2Um+0x53HSTkAIw8QtKryqsaI4ArYAjAAGiSrX7NSUl2h9qQxzTqkihWu63BKExthQvzZU26xiDADb4HYBZench4K66hc2EXhmG+KDlX/p2fkplYxIJB/PE+DsLa2r7DUGDkrhbIbn54EQ8cCaES/4/3h9lyUdxhsnwNbRUJiWLiBb1evzaGnS4fD58/yXrp8HRjqeDYQl0dWjRayVLwLR4Xx+WwgMVQLx+/NATZTXmXtL7Pt9kc0inKxkN1zvIlpXL0IrReMyp1SeX9Bn3MgEsRjl7mJgAPOvgIN2IaLMbZhqV14X0sLZrZp0IJpZLlIJrAFAgml2H9AVZO/3g7AEaqr13eO+3kouqFjvznWjfnIOb/QEKQzrAB47piv8QUdgOdBNNeWa0wHCC6ru5S6xEYBQCOJBuxx9gFRAjcCKbwoZxGctLdv4vJd+XW+yZGsFqWAnXOXKSdpovRr8hrNzBaD+vkvN+PpDndATny/lWXNkQzNUeJGkf26P6IbOfm2zwNYySqZrYJdtVBsoAcmRXH78PXEyeeXiGFGBtqXzFlyfgu0IXZHzXALuBApQAECb1S7TpgQXjMlLXRFwlM009NhkrAHTFozuhNAM0EoYCbRwjUE0uVtMOeXsuQkI+jSqITw5C6Tw6Ozde4HUxO2pdTbf48zL1Ib7EOpzgYw8vRdMWbTULQN+BfDQvrgpCvmaddMHE7/oYDWoLJM2HBVuNDDel+ReLVsvyWVrFQ+3AKIxoZ2hvT6BVJnrZNRgDP6Q3exY22XjH0ufgZYtqxUBUgEM194rwn/EdG8y+A94EQAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
whitePawn_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA8lJREFUWEd9V1F22zAMo46xOe2Fmp026YUWZ7tFvScSIEE5XT5aP9uSQBIA6TG+xnGY2TCzY+SVxc/v4pr/hg074i5fX96Y9+fK+Yeb+07+fuzJv7mXL5oLTsfWgROfHxxobYxvgKzAEhCOa0CwhwexLPQDxzxPFyK6ykPFLxsHQM0fo+55zQww2XoYAs0DPK2SwCoT0ZtllrSCGoQnsBJ/AhDreLuKmOkmHCmZrzkGOBSZDPDKobpeACjm/ihDn+xB+JoFgemH8sB8ByUlt0nnhOLbKgfA/KmLWfuTEv7D+gmwmB4kZT2cC9zQ0XBnD7gy0MjGGp5hBMwl4txWwkwSg8xNObnvF0SZ8gMMiQCJEZUMe94vTf3b9ZHaLu4vPhKSKm/xEnxF6UIk9YvagIRS/xngfrtAYsMzwaUTRJJfSboQNqQUMn3BgYaDrAiLOA57fL6lP/Lwn9ff9uf27kAIIlGl6xUvisjIQMJmdjJz4XbBcLPn/S3S55IDkQKZ/bg+7O/93Z9fPvZ6zoQ3AovrTDdtBBrNBZrnB4D+i0JJqY5h2y+WYkmwgCgIqgIQr/qBb0022H5/E7fWkOKagVzIBSolX10bm5dgHOmf7lxVhzKa2HxWY/+c7MeO0pzIB1cD74OR2v9a/r4zonMLhr2iuTxvKEUTzmHb9SkBgCONA5V4BuEyXBR4lgFNAxlMQmatDtt+7WktYUDnxp7JpVZROCd0J+IrKdY7TkbvD1oys8t1l326grhj5oCtvlQQTB7Y1FuE2iqoQfl1RRy2fcwM0OlYMm00Ui8SihlI9zprTK0xr0nG2WDYcZ35OYCAduwBsq825Qh4+kBaJftAzW4rphCm2QN2TNVs1z3mAJmCqu3GGp0p2DnFKYQJyp+1zcZW9rxdaraCBb+SW3VN1pDajPqiGUX9awYQNXWeeYgT9cOJWNOv94AX88K63OctnDWfNRmKQ2NOwcvAGuk90BO0OGHI4YABEPFW43ox4EcAzQfOeDPPiC7ngOztPVvakglCocbsWE8EQGdukkQ+LvxwHpwje8XKCgSI1fV4R11nZsszUBrt/g8v8FY8e0Dz3uwJ6kmUeDhjtJmUZ1MJKete0VtwFHDY43PLQ9GO6stpMUI/h6l13PAIm0NKgGmlKPjytYU3oNoamBdZnrxBBlSdhE6qWFXiQchAUnVfv+F4JAtPDWtcReDYB9+OTA2+LepzD+2EYeonCY9bjYWL1wxUzyiNw27kY5d5DSnXGeDAGss6ETO1nJYDXJG0WA9GcdBL3nK6Ugma/QNkFE4BUJn9YAAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
blackPawn         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAApZJREFUWEedV21i7CAI1KN0k7T3P06bbHsU35MPBQSy7f7YJEoAZxg0tdZSWqullFZK4WvRPzPsWgWvSkcYa3VtouWPlZIEP25iNNgv3aSJpSl7fCAzlSehQQ7kU50OOX6/mkVhYmIiWjlgfo+cbzFGvenB6Ir5NLcIeGmmbOSpR7M2cab0hvhsJfSqjRjmpyd0DcBcz6n1i0NuqJM/Y8W16kdL1HhTGTfK0pWwGC/OCRnQFFX38djbFFEr1/flKOpe4aiCUbUWCH+d+3Y07igYFUh7LQnj0qEgr6Z92xGGIf5azudned8+YPD8efZsHEqdVfa+EoNkeapl37bWW+lU8CTh6zrLsb9DYE3HjVzl9GqqR4B3ThnU0sONjMZaegJrmS39ksjj11QsJ+tayv5G8Jt3MJUJ+6kKkmRNbRc3o0AFEVhyHGqgL9pQyn6vZ6wGhTbtwlQGHjwxd8fjgD3OvpVKkeSGepkQOkWYFI1Y9f7oSEzb6+ei6pcQ+13V1l3eX4U13/bgkLnZIhQC7jpWibMfKWt3D7ByxU44N6LB/SuFJJwNCpYVkaPhzzgGCoSQru8z2Vn1yysFSlY2MkLNRys2ZRpeqf5sRyAEplZnQWAi/K+rt5SJALqX/CdlvOTiqGDN16MhS2A0CaXTmVZMgYkdrYQ3JJin03y/P5cmlGGBvL52JBOJ9SY0tkPlH8GEYgy+LyTRWL+ziSe9YEaxsMOMPMzSvW5KQQmKWncLw7ZZFRwCzc3H+xC4nh0J/5fKsDas927Ug9oPtpBVnhiSnZZDIc7RH7O0XqPukwk6+q7k8SDz+y+jaMm/ETt3bN6C6zhSQo+b57c/OLWgLC5Sn1IFypM4xZjjpeyPLiMpfSab//j/A5G8RzqoJETPAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackPawn_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA5hJREFUWEeVV1uy3TAIw2tJ0v2vp0m2UncAAcLO7UzPV+JjYx6SIEOmTJEhQx+m6KPoiox40PchY+ii/+X/64PvySPxpoZo0R51aeC8H8ZudSANYr1dwhd+/0+uivo5wzmLKJyNx9rtTvn1Fof7RZFSQuKvHgWlDI+RkzFhGM5Yhld79v4HOdSX9J7dRhTqXtQI5Uh/I6NI0JhDJvZE+jPrUW6kxhwDAnyJDlchHQfm4fJjp7kUdnZOhxJVcbXgrgZoNvOJFYAuNhTCIrWRX78vVz8sMmRzZ8cxYLAzwkAD41SZ8K5fS3UJ6hT4M6CGgaj8nuhWDJQq0O6nvmMG7wao+sE2OteNcJKVGRywmrvOA8VVEyLPe2e6myU6mBghR9yB/9SB6zxlOtmTtoq253EnOhg32LZzmQFHM6jWatXNnedZkeoZGXK/v+U6f4ly/37fcipoGSwAzTtzSAc2yIJ6LlFT9HJWWd5/v7dcxy/b9zQnmk5+OJfl5ejrOZMxRa7rdMU0lWvqYSAMrXreh2L3MrX6UyspEFq0HwxO6ollwNVwsR+ig/ie58lmZc4mond0GA2bvkO9/JpQ9ohB5DqOrukQSItxTHmewsBKzl2WKeBNwRpVokW5S+dx9ZaFwDz1zn1bIv5XkEECd5iEaAELUu2GdmqpE3WTyPu+pBal3Fn9pRVm17ROwI1mGxzCRDl4HmfjejhptQdmuK33Ltv7S2WAL27CtGdG06lOpBZJiRBrUxuVwBqSLpdw9MI+yaTwure9VUETjhKkUMHmKrf1zHAf/XS/Z8BuwfGcB9nXnT6KgZJRcfSTSjnoiAeYK7t+YCRbR6VGlx+aSZNkEbmVAZuhxfFAcw1h/5wcvrsbVguIHqX3AIy/UbcoHjtmfE8O/OTALiHedJ15x6WK2DuHmkwn9E8GcurCIveaiQBhzHxBGS9DnwPVrRNKmLhR5TStcCl77pvmf4IwKJNjOObPpOEGM44QHSnFpwe/TESjDSdJy5Rs4D0H1Rp2mt5mF7BUTuN9ctI6YsxJymW3Vo0VurDKeb4jIgMjfT/kpxkivExsqv22ttpIzwbj8602VHvuuuLs/0PTVUttzPUBv14TbbPWy/JboU9TCWM7BsWDfab5DwM8DSRI2zYpE0C/ZuLIiTdcp2eN9OhuEYIny9HMVK7PqQ11Dgc4kc7x6MzD6T+wABpWDJ0N61u9e1TLl++WrWXI/YjjL0RPOgmoSEbRAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))

whiteRook         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAxlJREFUWEe9V2t6nDAMlI7RLPRCLblr2fRCAdJjuJ9etuQHsP3R/ZGwxpZHo9HYi/BfPwgAKexII69/2jhtjNM55aUDIIN3YvcR31/pZyqAO4vrZQkILY9GVht8MXr7rZNQpOgi/usldCv6GmgIqQf0ex6+w2A/zwzgH0NUuXS4ssD8v+iMFtLsky4okI7nlB7Ljsc6pYQI87Lh9pzStBxIYY7nnB7LhvtzSpgQHu8b8tj7htJ1VXru6602pMDTsvMGFGxaZAPOICXunUk3pQ0NAM3TpIc6EQCupPRcq/pY5wQoG9GGgLKAH7kVhPq3Hxt8/Z4loAK5UuiAgegJDAAAvi2f8Oc5K6sChkoiiBEQE7z9/ISvj++8L5WtACColIQfqTVQ1cZPFsptxOI6GSUxMWKH5s3Lrrx4DnxiUZCnXkAv93XWZEu2pGqqMe8kfxRiAtJMHdTI8pIcTvLKtQXEAgf1idOX3F4CiDfnRTXhAjELU530Sif5PbVj4tWiM8tXaNBzLgF3RAwaNRV1EWa2QrHX5iPHr5kxGO2WpDSGeMBou8YPzo2oT8y+iheI4mov69fet3qOWrW+iqdyrA4GAmBqpxp7oyH+2P3CjmMX1Er2Mi2L4nKEY32wHcuH/UmMST2B3C9rhPRZ9X19WgyMqAWVO4HOA7GdDEI0GN2v4XJA7g0A0Z1YA74TVAZs1CpCY+ROexUAJaGuZiwYa0DdF9n1VIxaCjopvV+OLjOW1jkD2efLgcVewMbnSsAFEGLIhGIu9s4ZBcdVDXmarnsAQc58y1s7nuOJKuheIG0aFWg+kjtXqbmhgVhJBkD5qv8zEw55acOOAhzv/CiOUn06NNAQ1d4uN77I5RwSUMIunYYHpoYFPZCjrq+1KhcS6zq5A3BsPQFpZ5GLsi/XlXwiZoMPdSh2lRXmk6fnjRUvqHn/cL9yR5k6Q6mGKMLWycVE9ZJ//nRE2B4WI1lWPWue2us5329WQ+ePN0RYgVAaw/UqbGIeGe9PLbbCyLUIXpiR4fbIGwi8d0wPe8jdQetf2nFNR3C9PP4CqLyeNAhJ9REAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
whiteRook_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABJlJREFUWEdtV1u22jAMlNeRpBsCVgt3QW1Cl3Hdo3lI5p7yAyS2rMdoNB7xPeaIGREjYsyYk994FCPGiIg5Y+K33+ezfJ9PcxkW5bJcxd9pJmgZiyff4GM72Po95hwylEvSSm5MJ/C/7HOjjqDRtCuzU2/gvILxgY7PLixnDGQA58hL/ba/PrKP5jo4qIPga+VjCaZfKBMMhssZLCwhUbanF2kb0VeKc71C0X6XIa0yYQiDe2CSJeQ2HysP8DxXfLPgY7hetbYtpZ9yxkeo0qoz069EMBdpDwc4Oyq/8OLyjfgmkmBAEcK4wmB+eLrw2FnBeuEAS+SeDrddJqTRY5xlVsaQA46Qp2RlaFCe6HSXnQ5VxzgPzlI1kpAE1LsD3B0zMjh0gf1T1eStizniem2x3a94P3c83B5nXM8j9scFf8/nHsfjwnf+3+9XXF97bPezS6BuMkb8PcYcC7ZUSyxm0vJz4YAzzhcd2G88YP0ctyvOrx1Y2x5XvF87HKHxRn9GTZ5hwdgFyoELXYQhTJ/PTa+aJxrxxk4e/Cf+Pn8JbcxEV1GcUl4zJQAhEasyC2nml1x/Pg/AKFP/xm8iciRDGtXK1nb/TSdGxHa7FHqCrQgRtW/mSAdMn/omBRPRYph4v47CBuqHtmUlncx0SC3C+uugArT5odoMJSBx85nq5elQjs44X0d1AtpnMW7C0vhAqPvtjSDQS5/pVa7sNrrAmVLMyr8jMpEl8CpIDS8fYIrNUPbbqXlinz3cFtiKeyoDZC9ybCFX7MbnE61HSHsaaoYszqSHx/298Lh4ZQFfb0f5XGyh0tyTNFphiUhGcgLbb60308J6JV8Qx6ZjMSQQv4z2Gtk/HKgAlXdsgx5gna7npom2jGEdnn7sIB/ztoi0tIOUh1NQVKxEEDNGtwAtyNDGjOvr0Hhb8G/ujwHCqnGNTFlbODSVT21cVNzTxvNaPbMUHbSbJUA6lyas7iP6SxGpLT4mKMTPGmR2gR+ibiWKBJvKF/7nPKDdVkzenxkC/a5b0OJdwt5miq5Z8MPgf1KXhi4Tkk4prSifckC5BGpwy8sa505q+kmdmUkRrTaCiwRFOqTd92vDGAaclrlPUuSgKtFlPJUg/cwEt6QeaMZtMjZdajbUZHypC8ivTcOi5eyCJqseg1ouqdazGQ4Uo4ti18WFQdUxS9BasKQTaXdSK1hdmWY8Twhea0t2kWR5Y6pk+dI17Hi6ydHcAxsFVKqtBRai5H3ACtr+WiNw6H1K2dauah4NpjfmgN92g0CWLYLDyDmyG0BiFiOcByVe1XlURCIZ68GalqJckM8qK1XkPsCj2+xIN0BKcoLcIGdLl0mU5gtfzywecy0lmOdKq8oeuy5dX1aq9apKM1KukWE1Q6w/CsRIkyWLLy3LpUI6X/cXkZWh+8n3rgfbeuEr3xvdVbjMZAZARD0JmTGQI1OmdPuWpdlUdGzaMyFZbEqz1SwoGbYIUmIn21DDi5sXmnX+xXqNfWWrFJPUjfQEpudP59cS+E4h2aJbHPuuWKn8+Hklt2TvafhB/uuo9a3KylHCxsSX3/8AB/dQF1nF3LIAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
blackRook         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAArdJREFUWEelV1mS3DAIhaO0JSf3P07KS45CCm2AhCX3pD+mpm0E6C1IjfAfHwQAgvz3zcdE8heAtHr8THIiAlCqp4Lqv/268t002sXYBtrLpw7e7tapMoAkbb1Bz2x4ueBN/ZLEp2BZ4TngK4xw0ICzXEift2Xo49Ae806ySh/fwdvpT7RcCi4g6GUmFDwuRNi3QMd94r5FYtud94Fxi3T+PREJIIRI53Vh3AIhIBz1/X0OFPeGWWqAAwIXu89UFBDhvA6MIQrGJE0xItxY/Ox03Qf3N4CUB0D287IBjk2FgfdGDrPy9DgP2PdfhX4CbroJ5wFhzgpA/tv6lKHnRH+uA36HHUh135byMyBITYQ9DSqmamWoZUBNELedRNmayaL4molbLTS9mbJdA2xMVUfRxzRkPldOz1SxaN9MixbkM2xTCApP0Tmdhn7CcNuOqNSZHxrZLEYHBERAoiwlbuCqu1+hVSdhH5dE5k2z6gjrrYwHU09wtOKd/VQNXc7w5ParFyJC+AQ1Y/uxwvBb7nPEQ3W5D1hOW7gpnu8BlYbUeSE4TYcSy0Mo7T1Bsr6rvLahsWNxyrC7JEBn/LZLzCigMj68brX8xA1NiAZW0UxCwD2XLBxlAsooHnRY0eto5gbEWn1SGPzv0Sm2K2eBSdMKatwkQhCocFq3eBTMxvEPNMAnYh6YrXTLkk/KWcH+XQmWHeoL0CBiBIifegyXtx3GAwKeEzpXThoeV7ejGSlfz7VWUU9BSTtz4xyuanYi8X8RfD2zrH5ENxmJrrQDmtOAPhHzinQVe9qGWMIiqdGYQDBFIJ1+5njW5JnpIps1J3qOt7oYrVts2SU0tzVn/Ov9GmjHAh56FThloKefmE7Cb3z2EFuzZpl1Pzh1SeuyN9eWd+rXB3pbIekfVDPzk6Gkp1MPXwvJP0owYzUhekWKAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackRook_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA8JJREFUWEd9VwlyxCAMg7eE9P/v2cBXmo5tyQfJtu3MboGALMsy6e3W39a6/umP/Cs/5X+swZR/yBpO5SV5zBdvC3rvrdvxvbXbPnw3IOkyRVQA6ZvLI5x30L3deS+NjCFFYNwTABCvYrjbzdAfcVZmnC2PjBFknnZeLUiJXmLv/ZbYnYrtSBkXcmRhbCoB2oBFpqtuy6TnDeP6rIRFFvxZW9r7r8CIvD9zbCdHTnmojNWc9QzCaURqgc0Os4BsTwDfD2Ywu7CqSkM7xhQZ+JYKaEHAaVwCBymvMknlUPSAVO1lkqompiI2YV8j78EZU4fkEFnOYehiHKPNOdt5Do1yrtl0bE3lcZyYP4bSqmvHaJfMO/VWDJaZEKbDrFrl4UYlDxvjVJ7l4BOHcbtrrTaOQ7eWg2XeAIROVCOafNOFitB9wO3naUgCwBg0GjXXWVSQ07U+7TxOj0+AOuk5bV6GqexNP8CTnPG+exvj0NnP+rSf46xm4OKxSK91tXP86HdJRbGevC9n+i3EoNCSill83F9ZyAm16rf6LozYsjXn09DAICtOHg2pcrIoPPI1NPKoFfpQuAK3tRGhn6UZNY9STTpEGYZ/ZzEWf7ybKltVvNWsVyrMZc61tTRj6dk3hAFxQqFTxPVSz1SxHHJoGky+dL0AGcgseng97Oab19oq5lAjSBxk1FhDFlLqcZihn/PyEitEPQRoEJMPyFeIIvtvTm23inBD0RMsckiyXaJ8NxsI1Ns4V92+R7Li2liUshcgrIbduLh4rctZNONxzaOIQLjujdSHkqtY6iGmK7HdKhYyYMNqz0ijzTCKTbnOHNoxrSD3c2LPBwoDUYLPksgC9Of3TRUTw85O4qjs0R2z8BmlGN7JtQLsuuB+oO+tMecrYLkPKCiElyynQBmDKajU0yXVAYGI1y7LQoaC71plv13sPi6lyW857EOtlS4IL+Ylzzol/f9fBsLVrQq8T292z1T5zRhl+JYeJHxpByxN49Xeonx5W3SjoG7TjSa1DG9Kj22NVgewl7A3opo6vZTS3627vXh97+2Qlpy7ntdoesA3aK34gdCcAaXv6AUQSagnXbmlB9RO6DeHBMIaTbTm3BFfK8oZlBTwTabc1exgvDhESWdje9Rpbl1xATVzqo4Y7xT5Wu46qLf1cHvog6Ll25zbLQ5Jbz4Fb7mOw7z5ZsQk5bZsWpa7gtSrhbvf8dwVM4hNgG9mFJWfrNgH396Uvlwonm65v57BYl72lODeU/wvtRsL3npJ9t58tvdOBoJlf8TrTgr99yoHAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))

whiteBishop       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA0RJREFUWEeVVwly2zAMBNtX1JYnD2qcvjVxPpRa6jfYWRwkSIK0o8lMZJ7AYrGAEgVPIqI8jI+j+8eFl21vd0xOnnGfjeB/Sokoj7eVw2JjZPr42DJRovNgQKJEeXSCDzNb5VLc7xZOrktEKbeoHOp9xgQl2q533FoXuffo1IKCvKyWeGRlHTzPKbFR+G1Obddd3GsMDkLgUG9j13ugd7P3uvJ4v7C9p9cv+vf5wvHDwOn6RT/TjzQ6M4eCOcB//HA4O/bVAbztty0zX+C97SGiX693/n3cLoSZkRNzphfIxMXIiLp5v12UWVgnW0+///IrLocHeD+DD/0zp5fhHBOoTwdmPmKI65iYEnA+PyMlD50dvS4Z10Slt6wDoky7dYyEmCChkFfx3EVU+RhoSjVuhMoA0QurRLSWgg8egZIBDaAT3M0ysVueQZCCvRi642LbpG/4J0hkOv/ZoUFd5OSwyBzdOpFCt4Nz3yV4VR05AvE3VcNpVZ7Ha705Lgs60jT75Ae0v+EEExFCJBbwP1ZFCNKkmnRQK5qLWAVMKjLMocuUs+Bh+R/7bGxtHW1IyBufsAVZIIKUaypSpu2tSvGS+o6oowGBgvSVDRkAS9l7pCJLdabt2mmAT+nQMUbOzTQBntdoDgFDb8QTPx5KcG+EKwTOjLb2+j0GF1KxqLZbvlLBPjFL+o+CGdQkl9WHFSSTPyZp5ULhwTMk8EIUGRKN7VoLUk4cd0ZC8q/KcV9AJqKmW4L8d/pujogKig7ImGwXGoKE2qC4ajjcOzEkdt4zWLVgf98yvJUMdD0fk0mNybUfeJDRUgLW0NcjEPtSApT9nIJcAqSPsLAgMuDCotdtgrRinfR/dpHcppXLx0mPsHnnV9OyxyGoLXQ/b81nqWRFfKz62YxIMsTJumQfopoZI94uBH3GC4BcgLpvh9ZQ5bJ2RazlKlIAQtTR14F2d6mqEWFq+62S69SvNKdNRigSSi/e5UgZqPyahNz1aAMIaDlYpQipYx762plwOEwe+KMlfGoHtyTig8nIsaqDCxHSShTH/lllXIpIyfQgIa2JWa0xoTDJDPPaMzT4hqznF6kavkYDJwSVeraFsDJ+8un73WjRf11dvzkcNBxSAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
whiteBishop_green = tk.PhotoImage(data = b64decode("")
blackBishop       = tk.PhotoImage(data = b64decode("")
blackBishop_green = tk.PhotoImage(data = b64decode("")

# 2D Array for storing piece locations
pieces = [[0]*8 for _ in range(8)]

class CustomButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_green = False

class chessPiece:
    def __init__(self, pieceType, team, i, j):
        self.pieceType = pieceType
        self.team = team
        self.i = i 
        self.j = j 
    
    def __str__(self):
        return f"{team} {self.pieceType}"
    

class pawn(chessPiece): # Jace helped here
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Pawn", team, i, j)
        if (team == white):
            self.image = whitePawn
            self.image_green = whitePawn_green
        else:
            self.image = blackPawn
            self.image_green = blackPawn_green
    
    def generateValidMoves(self):
        # define direction depending on team
        if (self.team == white):
            direction = -1
            eligibleRow = 6
        else:
            direction = 1
            eligibleRow = 1
        
        try:
            # check if pawn is eligible for moving two spaces
            if (self.i == eligibleRow and pieces[self.i + direction][self.j] == 0 and pieces[self.i + 2 * direction][self.j] == 0):
                grid[self.i + 2 * direction][self.j].config(image = empty_green)
                grid[self.i + 2 * direction][self.j].is_green = True
        except:
            None
        
        try:
            # check if the space in front of it is clear
            if (pieces[self.i + direction][self.j] == 0):
                grid[self.i + direction][self.j].config(image = empty_green)
                grid[self.i + direction][self.j].is_green = True
        except:
            None
        
        # check for both right and left directions
        for k in [-1, 1]:
            try:
                # check whether the diagonal has an enemy piece
                if (pieces[self.i + direction][self.j + k].team != self.team):
                    grid[self.i + direction][self.j + k].config(image = pieces[self.i + direction][self.j + k].image_green)
                    grid[self.i + direction][self.j + k].is_green = True
            except:
                None
        
        # en passant
        #if (enPassant == True):
        #    if (self.team == white and self.i == 3):
        #        if (enP)
        #    if (self.team == black and self.i == 4):
                
        
        return
    
    
    

class rook(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Rook", team, i, j)
        if (team == white):
            self.image = whiteRook
            self.image_green = whiteRook_green
        else:
            self.image = blackRook
            self.image_green = blackRook_green
    
    def generateValidMoves(self):
        iMatrix = [-1, 0, 1, 0]
        jMatrix = [0, -1, 0, 1]
        
        for i in range(0, 4):
            curI = self.i 
            curJ = self.j 
            while True:
                try:
                    curI += iMatrix[i]
                    curJ += jMatrix[i]
                    # handle rooks being able to pacman vertically
                    if (curI < 0 or curJ < 0):
                        break
                    # check if next space is empty
                    if (pieces[curI][curJ] == 0):
                        grid[curI][curJ].config(image = empty_green)
                        grid[curI][curJ].is_green = True
                        continue
                    # check if next space is an enemy piece
                    if (pieces[curI][curJ].team != self.team):
                        grid[curI][curJ].config(image = pieces[curI][curJ].image_green)
                        grid[curI][curJ].is_green = True
                        break
                except:
                    None
                break
        return
    

class knight(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Knight", team, i, j)
    

class bishop(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Bishop", team, i, j)
        if (team == white):
            self.image = whiteBishop
            self.image_green = whiteBishop_green
        else:
            self.image = blackBishop
            self.image_green = blackBishop_green

class queen(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Queen", team, i, j)
    

class king(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "King", team, i, j)
    
# Function for reverting greened spaces to regular
def revert():
    # Define global variables
    global isSelected, selected_i, selected_j
    
    isSelected = False
    #selected_i = 8
    #selected_j = 8
    
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].is_green == True):
                if (pieces[i][j] == 0):
                    grid[i][j].config(image = empty)
                else:
                    grid[i][j].config(image = pieces[i][j].image)
                grid[i][j].is_green = False
    
    return

def placeNewPiece(piece):
    global grid
    pieces[piece.i][piece.j] = piece
    grid[piece.i][piece.j].config(image = piece.image)
    return

def movePiece(oldi, oldj, i, j):
    # Define global variables
    global whosTurn, enPassant
    
    pieces[i][j] = pieces[oldi][oldj]
    pieces[i][j].i = i
    pieces[i][j].j = j
    pieces[oldi][oldj] = 0
    grid[oldi][oldj].config(image = empty)
    revert()
    if (whosTurn == white):
        whosTurn = black
    else:
        whosTurn = white
    if (pieces[i][j].pieceType == "Pawn" and abs(oldi - i) == 2):
        enPassant = True
        enPassant_j = j
    elif (enPassant == True):
        enPassant == False
        enPassant_j = 8
    else:
        None
    return

def left(i, j):
    # Define global variables
    global isSelected, selected_i, selected_j
    
    if (grid[i][j].is_green == True):
        movePiece(selected_i, selected_j, i, j)
        return
    
    # if selected space is empty
    if (pieces[i][j] == 0):
        print("empty")
        return
    
    # if selected space has the wrong team
    if (pieces[i][j].team != whosTurn):
        print("wrong team")
        return
    
    if (isSelected == True and i == selected_i and j == selected_j):
        revert()
        return
    
    # if a piece is already selected, hide previous valid moves
    if (isSelected == True):
        revert()
    
    # select current square
    isSelected = True
    selected_i = i
    selected_j = j
    print("selected", i, j)
    
    # generate valid moves
    pieces[i][j].generateValidMoves()
    
    return

def right(i, j):
    print("right,", i, j)
    return

def generateGame():
    global grid
    grid = [[0]*8 for _ in range(8)]
    iLabels = [0 for _ in range(8)]
    jLabels = [0 for _ in range(8)]
    k = 0
    for i in range(0, 8):
        for j in range(0, 8):
            grid[i][j] = CustomButton(window, image = empty, width = 32, height = 32, command = None)
            grid[i][j].grid(column = j+1, row = i+1)
            grid[i][j].bind('<Button-1>', lambda k=k, i=i, j=j: left(i, j))
            grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))
    if (debug_mode == True):
        for i in range(0, 8):
            iLabels[i] = tk.Label(window, text = str(i))
            iLabels[i].grid(row = i + 1, column = 0)
            jLabels[i] = tk.Label(window, text = str(i))
            jLabels[i].grid(row = 0, column = i + 1)
        Labels = tk.Label(window, text = "i \ j")
        Labels.grid(row = 0, column = 0)
    # Place pieces
    for i in range(0, 8):
        placeNewPiece(pawn(black, 1, i))
        placeNewPiece(pawn(white, 6, i))
        if i in [0, 7]:
            placeNewPiece(rook(black, 0, i))
            placeNewPiece(rook(white, 7, i))
        if i in [2, 5]:
            #placeNewPiece(bishop(black, 0, i))
            placeNewPiece(bishop(white, 7, i))
    
    
    
    return

# Function for debug hacking pieces
def hack():
    if (isSelected == True):
        for i in range(0, 8):
            for j in range(0, 8):
                grid[i][j].is_green = True
    return

hackButton = tk.Button(window, text = "hack selected piece", command = lambda: hack())
hackButton.grid(column = 9, row = 0, rowspan = 2)
if (debug_mode == False):
    hackButton.destroy()

# main
generateGame()




window.mainloop()
    