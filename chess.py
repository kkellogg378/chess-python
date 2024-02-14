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

whitePawn         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAqNJREFUWEetV21OKzEMTK7xuogLUQ5LuRCvrThGkL8dx0kWif6Akk3s8Xg8WWr5s08tpbR9tLAN/kw+MRhvqw1znEylcW0/f3MBHAD5ylWMewPQBEZSXeSk1lKaW1QA26pSQP2pIUatpbaGjZnFNwZwx0DWeNRHmkRdFTNpbs+uYOGWn2+6RN/Safl6EXLmWoC2GG0R1csnSGk9FhWzzOcgKmY/ZLyDwKaQE6Em/IfWJ4fuHy8dScf1XnO8635MGchR0erj9kKG4NoEbbtcHxjvFxLIWjCjj9Yft4OtyCBe3r7K8/aKmYGJCJ405T68A34tEI91UOW+QmahtfLv+r98f75ilssAYhQPyE+kPlchJEOyCczzdjT4TmutQNPR1VzNvhUEdqi/y2dHp42zEES/hGVLTVQ0tmF+3QQACYqw5DXgcxOyVg4W4nK89WEt4NZRIomMe2GKFkRZOH7FBJjPP28KV/bJMXTd5Oh+FGHp8n6vat3pIFYRFD+l1PYTxWR3JTJjETtGIXmvYVKi9v6sEQCm2Ku9+/Z+AEAgDI3eLPN8PTBAb1XD9uS8stBQSFz9euQyYf5CA3YcDt3ZlGS1G73lMPUPFUA8s2tj54qtlOM9WrA4RvaqymkrWZzuzDQ3a4eOIh8/ZT4TP1pBTf0kJicdmglloLvi3IZTGsD9Yf71MsGB5EvDjyKu2UvprEo3OmYUYhB6hUbzYc/AZa5eZgdNKdjxSk+nGABAT1A9vGLDzOkHrkUGjveeCY5EGRkYO7oFMPQ7xJCkyoYYCet7GE9YR2qJ3xyAo1w3DNVzDBwlMWbWA5oZORo8XU1IAECZpSq9et1Lh6fZNJANix3KAIjlL1vQ0auErf7RMk/Z/qPME4IAdq6nnZrcjj5Cz+E+8g8RyVE5eZCyfAAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
whitePawn_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA7FJREFUWEd9Vwly2zAMJL8RS8mDbL82+lBruc+IOjgWWJCceDqNrYM4uAfY29Wuxh/51Vuzq/5F/ugHN/jv+DL91rV667KY/It1sJLc+2mXPOQRNYi8ULPK4N0XihT0N73PBXhArMhRNIXrslhY1MJYeH24ZNFb63ZdnkKK8Zzc9uL1NSRSumY3ajxJgOrPBvrVS7tYOqJJanaWFG72btfn5+l93xaLI89eVqiFy/9RRFZCqaHtmpy1SdcYtofAxMDSLktUqdwxAIjNuz92J1ueHUoM2cJWR7fqCJMrdFHEEeEjmnNfuVsSwVpOCAD6tSPUX+pQwgRJBmgKKevW/NpiBp6DGd0YSMyknns+obcmhF/vY0+W9Na2x6s8yO2O77bpM+WjpZqx76NqyEA3D3EeOxEOWOhtf3oSJDqTwkxdKThBKqCZg5dqs+Dgi2nC7fGnvY8vvb7dT0sctChCmbQFVXv/aVdKZM032Ovbch5bzSiC9PZx/9v+HZ/a4l22w98ZFXUkeleYuuSh+7pnzm8u4PzeU+48gi1oPUdV2+NMRA4tB+HNHFRHukiC/1i5QHblfWyl+UW4VQHVdpokYOwbPGXwCXkmvEDFaQD8SqIF/aOz8WvChvk95wFTHUoeW0BWGTwdLJQpaGQSMHrXrq57b86YVFv7TCqBdYDNCFwFJb0v+YyFfDkbAIr9caaL6vqr0HMnihQvnWBwN1ni/N7KcIF69vsZ4O1eiLpmojsMH5ZubjjKcOxPlVfzeVMzo2R+oIRjpyquyKy8S150sZcKRUqOh49UQ3tcE6BoaVApWks3jA4kLmIHccnW7c0Ia3x/HVvMTkKn23OF/sL6LCyGEh/JlpBBNcQO21fjNjqAlk9mREEKJ4Aph35iwAbYQWjqbvAsB1lGfje4ITgVicPcMFOCtj7R8QBc92gxC7mszp5gSFcRYu2o41DKA6ZoVUIdy+tMONTtjDY0qhyz05EHSPDt+SrzYUGB5lmd0r0gdymG0BEDl+97MUxXQtJ4uX17ntPZYj0P+twYnfIvMVbTSB60cwORlo/esdIFFLSWZPiuKUw9efklbbker1j77Sb7gKHZKEr9NFzoIScPNvqmjuVYYUE5WUSrJputVSCBihhQmh0zVZJOXTHuKq0x1+XAI7mJ2EQ5RQ/8oFkkvJo9e6KppI9jReYgRLFQrXF9qKQzoB8+fJ6xk1qZeflI5inFpAX5Xw6ldR+DSu5s2khXunBQAiwbUhxZoA95cNJl/wNPQFUExQX6fgAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
blackPawn         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAr1JREFUWEetV1ty5CAMlI6SMd65/3ES49mjkNKLpwDX1jo/E0CoJbVaNsLqQQBIdIB+0MP//LcHgf6cJ/tt9uiwAHgOY7ypWUEGYEu+2324np2AJaCyO7/bzcDeqZVln4tVWLQnAKpThr0pv/ppL/Mj9+Jdg0AESP8SSYPaJ8aDqlYceJZ4nzOl5utbetBDF/SQJyEsInO3dNHrCebArO1m/KXz4XUm4rnFHj+RiqktumZ96hLRZW1fuFOdZ/DMI4D4uYau8nJaa8nYhjP/uk6Rmyra0ev+gT/hzfFfn2h65eaWbSril7Q9ILU5F5ERA6PRd/yG9/nmnXhHDWyfzZIB6oe0ruF5hCSOyXcCQY+QMBVbRIj3JbiKFIqNs+aUYKYLCOF1sH82IiZhYgnBnFLxwGWYPV1SnnGgMgpH0PkoiwzAlB+B018Huhtec6QWgVNG4oINmxyoOl+YuXPXBeBRp1lDAGpFqbFkgXRgp6Wze5kdQ0ST2+iS4zgTsgwps5S9HgjlqXXucGuDeto09YZanF+mhMLH0nrzPCwyMBqVw44ZAoQvImPB36qgQ/Vafyt3coO1kWc3CSi8Al9pLI+fW/S4f6ZpLdIwNaod9IcC88AApIGEPWkJG+lF6t49Sg49i85rXRYWpcxBhOvvlWeAnNukU7fH1tmkjHxS9FmKDWQCVcAHF1TikQG4ZtWi/aR5QOTjVLK1SbecKK34DMiYgYWanK+gE4hFWAdQVRiqcZ6Ge0bTCb8ESu2+5rm2PP3K+LT5bp8ZRI5mIi6C2maA2i3P0TwJLfMGouoX/toReSa7+xNJrKcQWgDdK7r1etEQBGTtrxyrDOtbmZSFt4u4CwjnBckC8uARMgKw+2IYPsLy60T5xIlDixaPEx2YZCyTou30Z982fldMOFBNx2fdpIo+Kp2JVft6Vgj8CzaJaTtrh1A2AAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackPawn_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA9xJREFUWEeNV0GS5DAIw29Jeuf/z5lN8pXxFkhg2c5UbR+6uhMHYyEJ0qxbt//4NDMs9C//E1+/PFpruK53a61hK73XPUomELEYNDbwf3lbN+NvCeTrPHJHZi+JzcmOf7nDlPGAYySg1+TcfU5YgYw7jNv84E0wi+t4No6IvAdEfq/HEwPiPeu5bpUso0Vwj1OAIJ7GqQQiN0+XWe2UWOrNpZneGnTjh6xPNJILrXXfeq4rFuFMv1d05wKwFGIW7AmFA826BDGVhCTdIJPAzxpODBaS1qmSxiun8v9y3dMdKuBRUTeUpGoYiTeSRaX3hgIqOQk0+dSbBeTk3CChntA3J0xzduoBZp/jQ+GhUPdzF+NK8+oVzChoJoXa9ii9LCajkvwcJ6uh+u9I4u0ThgMp5ifZ0uwHiJdWE400vOngzY7zHKJl4L/PZX+OT+xy3UQiCDbOtztpml2HDgotNQxejMS72XF+aB5QSTqN3/++v+3r/Ir713NrODqknxMJaTJbCcqUMimB1KF3hsFcQNLNwKzZfV9Cs7f+MchLH0AgnLSscWxNAp2fM5BIp8TDzmwupe05ArkuCafWnCwMH2ABBjV5qgKLHStO2szO8wg2wTRFUkEis4dEXPtkJrCT0TnANjnpd2o00xHtPD/V/+KkAWADAUU9b82sNEgOCQfoHsk4umaRbZFQEDLKARTu2HyWGSuaNWOms05b+0HjW/WZrBjdAMTx7+NwBLBxnJIglhmxjIVGtd9kBKJLN9xz30aR6mh4MMxIpPg8FxLi0JOzydKexkSUzoh5oFHSQp21gfAUkVhvIKPs8lwXna5ZEyUVe3I4Ce5mT5hYIrkuw0gArfKMBNwRaSrNOfBso5h2yanEFV9GMsgjB5OFKOkl3hFJ+zN4kFXuIb8BWtlZjWWDU7NAEbGu6dg0SFeTDwcV3zYQSAlGN3xgs9VLhtvVrFtC0/HPS7oNENmdODwmuwiMt2La5pjkzH0AFlxwr8nMwMa/8oGNrbo4x0VzJzwBK1toDCoCviNRVK9+MhvZrDl9L5B16W4Y0bBhzgE1LXPWDoLGEhzjvmBKGEyg/XHA/AUCwshkBkB2zCTfaHo3b0RD466KPAfgqSCMn76wliSmPS1THlBLUMboM0Bs/DJYTLoSPXOaDq3HbPAsY4kkHii9khBoHsdZAyZOTwNR7ybE4RUFESXNJucWvTam1BiNXLISRTjhJOZLHfUdVecd1D39Pkwq3orccUW7sYIz4YtChpySRhOr9U13JtY8kjOMzohJ3nw3nDav/o6r+xuvGtRuNvWCrOAIqiNV9IR/O4lxAhwtd7IAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))

whiteRook         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAxpJREFUWEeNV22WmzAMtI/RB/RES+7apL3QhrTHcN/ow5aMbODHwmJkjaTRyMmJrpxSKvxonvu3WC3uWzFxN2t12rJZ55RygbfAt9vC/NMer4wiYGcw8I2dxpf6oXsQmc1YB5SzNbj6b33EOaUyNO2q1IMagfRAotIGUO9tlrIFLDY3TZVx0yrMFyee6tIcDXHAlVo9umC6TS6JaWAHm98ogXf4eW1l2d8Zd1Br2Y/8ea5leRwUgD5jHexZ93c+XltZd6w3PkW5oDZEP8a0YxNstsmm6uDz3Aobci+dAAporzGh6lwzhiPnvhJ/jLhr4h9f3+nf75/0IQQLmQg5FLTslGvHay1IFTvYRBNwY1xZUCH/y9d3+vsHIFJaHu8MoOzPetXOYR2MstQAiR3KAH1g1mppJQ0CRFOCt5s4v5JuJ8WupbucUBnEX8t+90IXkAki6JlZZ+m608oC5nhuBSBZKTl5VAbxo9Esj0/nHCuM32dcS3ApRbzB8Vwpo4UYwcXlF6gKEw+w0BF1y1OA/kUVIiH5CUpvj56v8kvp4IRo+VbUfnQFLS8Dsa/VuC5ERmI+/9EM6Gh10V/wW/nv8ZLvsfR+XmuhEgjz9VnTj96X5pR9x5MVXvyB5IoLGbLLcivJFz40gdIMhDkMXo7rZcBUOwGgfGFmSwxCRMyJOI64rLcA2A2JhOYsJVRQUvgOmGa06WMU69AUHBABaHOhVrukde81wG5vDi+SkNoFEz1yYHgKovW4G4GCOCudQfrv1eYcjHFmSjCYyxYZOPBrBfHrAGI+CBNIggWAi6gPr/0/4YD/SDtTDx0uLGIF90bLQFTFswpyFt23jInft5U2jDAUoQNsxG6FFiTRXAt0Q50Ak/o2JRxnKTHxhEDqWbzXA4qBUrOxv2uAIwwcivwOiD5qpBNq1WOYZicTIe0ZgbeUwWRmA2XE2sthZdhyfAjhSVeZbWa+jEEuBXUFwHBJVKCoHI+DtohEeSpE9SxYN9SjYa7DSGayaIJ3Ie2S+HTcXU0HhgkY2dw3CPTAH03uHEjmDO5+1N+VsxbDf2a8sTey2vniAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
whiteRook_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABFpJREFUWEd9Vwt22kAM3D1Gg+mFgNOWXKiY9hZxn+YjaaEvtC+Jja3VjmZG2jkO/Btj4r//HMeYYx4HbuLrY4wjn5ljtifx2Iw78dYYcV3BIgDj4BPf6RO3+Ba+byGnAikOX5zjiPv4XZGWBREl1kP6WA3P8kdkqVXiihnNGVGdWLyoTL0LvuKECo4K5V1wE4ilOLmItu3NY0UghncBbiFm+LIcTkC7SCRcksJ2gZ5rJPpYgSurRir7/GJ6rK8WE8zkwMyamhO550N7TmC0JxdaGfQqEGKWiMiSgkKAxBNCWTskJxJ6B2+lAo6MhKCd0Xmf5TEXDmxgSUCpoIYikVY30LEKE/QKpRyzG6UQ5MAIm/IurBgyb86jVIPgYqoJFPeen9vYro+x389Y43R9jOd9G9tlRzLPz/M4XR74HdfnC5+N54xUV5L/DlgXBKq2pdTIEMEuOxKJ3SGZz3NKm0nt4/lrw8aZYCSwp/CrIlKKoAQC1njVN4hX5hHBvv1IyB+3x/hz/5l+c74+0sSS/IFwGlxywBJTfWAk/AQFAoEg4Y/b7/EXyYgfqXw5yTHHx+03kziOsV33VBdMyQQ1q+M6ZBh1d9oOnbKVd0XN05bTI6zrZr3iH+AnGxdzs2XjvlWQQFh/KZVyNRKwu5RLRBPA/qB7JrMm0Eradk8/AAPqAXp9aq15t0rh0vRNQ9qGWIv3ruNSyWMMSywzx5dWQxVK2yyemkq8OOd43k+q4wsYvWmNUEnAL3fFu+XC1dTcgbMd1+KBQiyegBuV0LxLUb05847nsbhaJOstF02fLIk3H5Cna6fdjrOD6b09yGg2lnFm4znfHtWA1F/M8OypCkrTixK4Sxm3rN+7ry+ekIFkq2PCpBpVq5G1tp6WDRkG41CvipaE6h6ut74zpSxBupYHE6pkyYxM7D7wPu00Q+Z0Aw5sRcSGlKOHDddH3VXytErTdKCOLMFqto2SJbyDSvA0Y930N6Mp9U7Y/O+lpXsgeemGZLB6lCcJzYChDpBQ5SqAyYG4hgrir5wfBHV8n4MGUw6ygwNmejyR04tqhHuYiuh8sOQuQQybhQVatPmkyZpDbMc058EaXrCes+bQ8uIDbNYPNSbnUI7DXaEBue24ozKDHKuq9eQ8kEN08iMTyDkyGBt2HD7Qzw81gkeKMTdQRfUQ7F0J9Gma6KIbvhwY2mHEngP5WeCZlEe39TASCbAUmv19WHG5auhsBxNNv+xObT4YA9NP8kSnmZoJTLKWn0q4hSIaP8wjcVpU6kezl1MP50FOQ+npOp4tFrAUxVVkaTAXLl0c7teoo5HM0lIfEeO587cJu5xhmQvtByChWMohlZORfRkJ6JIyhJLUNtsYud9PGYgdxgPlmpTRSab3BI85TjeZk5DihvwzTkb/ORlrzGmn3poDDXIFsoZL7yVjeggPSdJAI/mcX5MqaDQjWs7q5Whd5wtp2/OkDMtFy6maBxM9VSUVOf8BKXQOGpT8GOIAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
blackRook         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAt1JREFUWEeNV1t2xCAIhaV0Yrr/7bR5dCn2AKKgaDI/kygiXOBCEOwPASDrgntxYsBbur+QE0E5Wx57aXovv1F4bpy3Z3xDQMjNl4k43YjVNIcEAuQKhfPg6erXwg2RFYTddT2Mj1F41m1C8MI3nCBDRxUwlx+9ztEgUjnGyi6GySOLy7ts5i18cwhMAQs2GAzr+ROAlG0FJf4r1sch6LxOW8rndSL9Y0Y4/g5MXymf94lkyFae98/Ouo/7wPTZ83kfgX7vzXMOIIBelj6Jq/+4T9RnWuA1MpD3EejiLTQgyIGIBno090+qRTnE3aD1cx3wve31OCH0IjKFDXKQjOU0ecbQXr+wb9+DTuvXcf7CnkRmMKAHAAkvS5cBKeqSGlHFeyg6TjjvS9OUPWRmjJL5CSLdr2FwShThLJxqUJzCb+WK+65iV9w1oFCsa2fkqXrfoRL3jBlZDZYgpM9WXWVvh5gKq1XvA0KLroOIYX1uNKgZBUqeLN3OBIH1UDm2SwRvG5o+zdZl4ghJXmr9D/AXPhhKbwKTOT+qWiQCsV3r9NZ/UWOTb5VPysaviMIOScSKFcbaD1q2iQF2lpiYYdANKlF2o7nGVgL1BUVDZbk/RB12Uu8NgYgkypr4I6JcCdZ6OyIgADWtxm3qyJxlfca+gK4ioDZ1k9sb/hcw5OpiwDpOlqmsAf1MQFqoU86opa6b3HXCsRl+lfq8WN54wIJgewCfnFVh2Xysgh5pGkoYOG7QCqDQIhkVITDJvzqTT/drrDDzUDIIRpAVz+JpyGpoCbooELlT4q6Fph1cERjtUtSO+0L/gdL4woYwHAnUe7m8Vp4xtrkvpqkabhX1uyauitaTTc12QCDA/kWjWJRFJFuu1GYziDUrzr8L/ZeWNb59Nw4fkPu256zToGYtFu6zH6fjvO28WXGDG8msEzM6HdcjCl1xsb9lHgJlH9fM++5gGGVIcG8Yn6y62t4/7R59O/pU6QgAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
blackRook_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABF1JREFUWEddVwt2pDAMc85C2L3/cdqBqyz7rI9tpu17nYGQ2LIsixUPfiMW/vAxf/JzPHlRt7UmF+hyxFpc/zz5ET+9bOF63shVdZ2XsBD7OAAu0xY8Vwty7arvPIyP6Uycwy+OIk/xNx2PzVes3LgSdXBP3siAmQmzGpHmo75e9xgwk8lotUjbN5oV5kB2oJUI49kJLYJ1lgYQ8QPWhG7k+4LXdSxAlPmziBgOAzwPzlzrX2NJqFmvF4SDI8h38KHq4DIBOpOBsCXsRNV1wUkqo88DAiKOEGCiPpC74sEsFfbr9QW5EReZCx4fiYC6LMK3GdsPTE6brUqu6u2ecdc0vHUH9WLgZIvgr0RU0m8eZHau2d5HXNcV+9yo23VfcRwb//NnHzvu+8L/3CfXnucZn+tTXHF5RaPqGCBAQArwwWjmsY8zrvsTe5/I4rruOPfRYCGoG0Hlhp+b9z/X3cowOqzqD7qAAwoB3TRJxEJmAKJFc8IXWgTic//GOdYmErOluZTlJofQBewP9rLlUMqmS2dCu1b8Xj/x9/hTbSiOqifJ+N/7J/7svzgkA6B+DFXQnkgagUCKq294AXE0U59nxd6b7VQAdSOx17K1+6A8nImZuLpnDTE53aLg/ICohwO3OHcSTNy2VKvV2FXZnqrpIhFN4peKtnCoO5y/xWZA1DrA6E1Cz4IugVuNVUySUlnnaBtKKAIk2itSCaewWjJdI0nyJCOqaulQHtyDWWTHGH+WTS2NvVviuU/eL6kd43Uqp/bO7JLl1vXWbB6CFoU2UNI9TyyKExAEhYBK+qVUNVpNxIYxP6UoAd4SPXkGTdTrk63HZ1z7UsFBUu7uErgpZzUsT2a+XATVrqWLuuEjIm6oX/uFRrfNTnVdmZUxIvOmJz2gftYgUyKwR/qujUGmTBse7JMcmhOxlpq4GMf6oomIkTynmqFbDKAUYgTLUMiBMTeFhmn+8lHkSvxDjhImNbhuVd8XL1KQDjFcjLaT0R7JgUpoeMxhn1qO6QlFKTejmFOqbIWSSh+JwJdZFeVqELnabUfbo9i6UaTQhmiYYRO/yDJ58EScmoh4ogxJy3aO5XZMEnTI7csRFCCjDSUlow3VaWWhM499ZAmcUWs/6rk4gNjjbXKTUO6WaU4k4DV9xM9uMsQ9p1fK8bF7+tUEbUd7jxFcWjC7bFoRTEOb0ppO/X7AwwndkeQrn6VW1aitItb7xIr782GJahq+Fb+FKEnY1k7j+P02k4aESbQEDiuFCfT+zhJ9hh9o2/+a/uwC933D3ayFGRkvPtZ8d3aJVtmOMRkj4BVbGSlKSES8fw2jQqJk92wyyc2i7K+AWgVLgPy2o1vpFxEo/uyK/fb1KkDzMj9h/muq6ZWmaupj3xOfz9tH2GvmeB5vkmOS5IoiYTdXvb5aHmTR7Btr1JgT40XDr85fhu1rgorcFCJ51DZ7w7m2NBv64S9Ng6EKfGvyHCYx27l0vJafFf8BB34dFX2aVnoAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))

whiteBishop       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAyBJREFUWEedV1GWmzAMlPYW+yA90WZ71pKeKIG9hvukkW0ZZEPKRwBjy/KMRlKY9GIiSnhsXnfjdUYz7zArD5QPRzt+yt5s8I7pfTN9E+ER3CDvnWydZ2JOlDI49jHPWR+3JM/T/SW34dVzJFjIRJwaRrxlb2hd5sTENH2PHMhbOIqdQVnfbubhKZ+Ok7ZlSknwS4ggODEwdsDHaPUUcGILxYjvamF9zIkUfLkSKY+CRIeKg1vitwFynQKzsi23lDjR9PWin783oMdEn19P+uCPYq/dVIBOXmeN4OqL8yyKqLy5hkgBnGn6eqr5n8cvOo+J1nJVQTNe/fe+r8vNgANFcvTP+1Oft8etjPmgDKPfZR6DLIy8UFaCgqikKNPQyAPz9+poPSpA47bNeT1+Or4z07pMGoKww6pa+ZnufvNYvBb7jb7+J4WQKCGnC8hwrZKO1CgE6dH34Rkk2DYcKmayVLIf1Gc3Wc8SE5g3/V5Vyz3u96etfI1WMNH2Z4b/ug9StGykWztZgI0EROw6MT0qJG1ieinsPrBM3bqDpXBimru14ehKnIhKeNVA8/kaSkAWBBOgH6eOc37vmIEDo5jECZCKwYfAnRN3K8GT2C707KRaXjNaAYG+FqAeIR6uOWAG3c3U7MHzKj+CumUlgASriIOyPIjCNykAbuKAAu8aFVHGHPUFJ3q85oAzsi1OjplmbUtECInm+/ZWIF5zwMWTZsCS1awa5wTP0p7t0/EYgrccUOhFd7vo12RoyfHtctx0BkXCsQQEfsO6LNMg1ByENXKbu0XpKE0gcBIoMgW9gLRfNlnaN6kBpX+tcaAo3F+YWX/c7rXxPaUgd75wFJkPW1V5eiOlUzBHgUZ7Qv82dACVz3Ucwn1pW2v3rqjAMy1UqI7wUFgdJajYAeeiQG/dNxKOVT5UdkvDdsZa7w0dlaXrE4Ls7P4XuF3tEU2oO2nZ0I6W+S0O2LHZ49QJSjv6kIKS8TKH+r/Bug2NBCBg8V9SsuvXlBalwBqYfQOoDmQvco8XF+FYQru/ja2kInXtxpq2vH6zpwvyvFZ0+7P+AeytnzKgtm15AAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
whiteBishop_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABBZJREFUWEd9VwFy2zAMk7Zf1M4+1OS1TR602tkzqh0BgqTstL7epYlliQQBkO79q432w2U3e+u+YsRi/YJbA3+xiot7y9V+r3NxXdvbVx+21K7TYb23Ps7xDYT0U9y9jd4Oz3qk/sHzeuuGABYLBe0bC/UPdizZ9rY9lmbhr9ctN+DJB1QUkAFj9zKK3kcbliQCMIg844Cpdy5wiEdBZb+veGZ930oBCsDYzvL0q2Sv0gEBfmHNGIjX49WDfuv5uChWlGO97oECILW9EHwBR/sXzjEAJwwr6/EE+bImow8guD1WQI9cETGJtb7vsXUmUok3kzA5EACWAAxq7F3J1tv+WHHcct3av/uF5B2tvd0+2+/xSwIgo0M7Z4oEuCFD1MsPRaBVGdzvaQeKRF5Y+/3t+hfBPj/+QB9GymCNo5Yqm/ngJZiNQNDis2h8v1+4sW9qEC63T0RnnCC7W7sYH0LvpoAk8VG9LwNIyp8JaUFgczcVBagULtfngcHFXxy9IDs45CoQW1NEMg7nRampkTCLTZTsGCihXCnljCnNzlGBEU02enasKkttsN+XDKKbAmRGc8CTazpqKgNLXQMwItbcimMpyO1xKepwv4eT0sSW605pyl4dnSRhmgyWyAeIYzrhEUq4XmrHe4EbTVgdnS+JGA9MvBAlLfwg4VwGUJ0PFXmaBxAi72h+L6Xph7/viaTnxBjPXly6YTaRkmqJPF3sCTQOpjUOJDzYeSUkCB8cfzEPHJl6DMh4wHxkVkyT+ud1btkvEkwOTOpJhSlsZ2YQ0flgzUbksiMtALpp0WzMGccS8Pu3RiQ3xAEBGbOAGblDyiotlPW2Tz0gWmtRwjw3FRLiIEfp+zGL4OxoxWmv6p9mRCIb3c55o30PokgZ+iDCrAttAwafcHprlCPXeNfHV7rsQEsuqiycSA2In/bZ+1d1czYO7x0xI9bfMAsUv5iDtunIJJjZY6lmSOShEbdYsSaiWsDJFzyl/YONSLmgIWnkche14M0NQbGK7Auec41PRNVcknjyZka7YQY0uD0ixxIICfjROKTWS9Zc1BGWX98LgoSucinaTt0fS5bEgETNbWz30PW/l3C5PTGWT3uGOaVLTTKskOpBI52MKcCP0TotQzFLHdQ43TG8obJPg04dyRIhruTYTeLIDPCionrDI3hQmVDjjUg/p0PW/kImQQV1HOdInTYr2WVn9npjL718pdCpoDRpeINTZhp6pl4QbJ1tFPDHdOwDom3uOzEGvlZN0q1fzCHxzjC3+nCRJKHmfHtV4voYQmt78fkJSdlrVfgdEUEK/l5IMPTm5LKEhx9JOJmfXk+cYCVwbp5G9Y20575f2nKem2f0bjt6LYOk57lhOussV71ypwkzUH1X255bkW36H08nlf2ADtrsAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackBishop       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAshJREFUWEe1V1Fy6zAIRL1JYzn3v05jO1fRG0AIhJDsn5fptI4ti2VZVjTB//wkgFQAyiJG0md4uVoKAG5JggTlLsIyQdxh3Ne8sga1b7mUAnB+r3QLvgtU90WGONqD7INM8isXfPf8HobJulDuTEkl/gRAsHuIiW/i7+21U3WZxALH91QQSQhBfHiNKOIkR+QP2KDMaT8FhAEOYWJCKOesWQssU4Q5SmYyQX5tdHlcH9jzm0GkAp/zAz/pJyxFKhzYf3BxXLtJ3Xzmop/j+qPt39ubbp22HAtJK4Ah8ZgJBNCe1IvPeVCId95bKAagSm/Jy8tGIx0Dfdj42/7KJCkuiPiABjsvI8YHJheIcG0D3AHYfuO6GfVR7YXKAcDcEfon7AH66WgXWYcuOTIbqpN2D9D4wP5lZeHBQcAhVpVXEBpYe9/2sQc8lkPjNC12bXhjHphp3tj9CLSRIh15+Kl/bHAxQql1dbBG3FqEssyxOZSh8ni0DvAsxUYkVe7QTF3bMJTxHEj0I3zQHnIezIXsFIPA7WKm6/51YcBXtaPeThfevUztOxF2oelLB69t6QUpea18QDXQs1Dv+6zNd1N/uaslqLWtD+6NaGT3mQhNq3bnQfMKmQpKeBCtiqoABsoDI08A+TcXO2/ogco9SCwMEedes2bAgZplT71ghEYj2iIhfVSH0gdDEGWHRkRVt/HE96sT4ebH90pd51swjp1bDXjhSbKYMpNuzqS6mEHcH8u4rteA2U8s1Lue1D866FqrScapwN18sGSAam4G3OnBJXZW50MCV9uXHdL83zCWwJuNqJ+pbXOgbYrOr+Mmkwl48IaUIBUdUUcGzH6N/rqqo70ZlO26qocmOlYK6mHmBbclsLTLJpKdOSxZjlHrJQh0oMa1BKAB6wjQROoLaeeDwMDqrZEF8YHQ9OZn+HB+Oy/Q7WbE64p/LY5qO+NdHo8AAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
blackBishop_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA9dJREFUWEd9V1mWpDAMc2aOAvTc/zhTRa7S6edFtgxU81MLJJFlWTZjfMuSIbKW6If9GLJkiV/4pffwxPWr/s51Q2TUYr3R18W++BgGgK41hozlAIYBcwi4cFBfYwgsgHquftteER72d9B6xrfi9Ud8h/iulAQXWAxO1lgy1pBt3+2veZ6yLPIAHoclY8EwGA1anEgDkJzR+XozAg9IFJ8naVcAY8g832IIwJRTl0nMhREr2DXW7gCwEW3Y8ub/b/vRtDLPGU9RRo1RBePMtkBsm+EAirjKPanQNnCKfb9tU+q7WJEKZWQt0/XD5eCZm2KA1RrBu+CgC49m2zcD8T5f8rV9eYBryGv+l7/yJ7OAaB14wMlqK5ZKhFSKrdxA7BDZLfL7pWAUyLH9swgf05HCxPoo7FaGARSllzkLRlT1qi9wqPdf821bH5tqwm/NeaavVDCsqUpF+EDczGci4azs2NyUnx5R0cC8tCQr2Gchs5fcjKgbSWwbFoHK2o8dLuK1H3jPebp3qAijAvQ7BJvIg0J3328rBtPms3LLZjn7W4CAW5oX3PLMf93L24BfrZg3SQWTI5n7ZcaKIVjxW1mALd/S3lNiqSgAnw1IgRzbTh3h87Ng8VQtoIjDpplBCNwApNasEXHd95JT99MHqHv0ThaPqxZ8n09uWrecgXAv/VRR9T7mu1aXHHJYJbj42Nbm+wy7rRvs+zcHcQ0gnkJ1b7lDrAPG4IAu2AIcIvOt/SAHCzqPU+ZmjFRlFfSFcWDlJiNWuAnA6ypp0LyHv8Xfbrlpy8Sto4tmxP05mw4trFAcWFoy+Zc+c87ZGlE7OElAd3RoWQV88HWQaKnWbqgaeGhe5oJPie6NmFqzJtWMqGjK9WTL1kDD7awSWPu0WNOjFVDzZci5DSjcjD4xAIUEtBRlzgLeDGDDHoIPcFX/LrXBYxVHZ8AVgD7XRi/uVL3MdBCB9bb6y+nRT/B2zJNRjWi9whxgSfWavwt12oTKp+7tFTWhYuwzYbDRbMvXEwMsaSBGW6bSs8ewuDqfRRbDnbMAQXbbhjHB73Ie8D25I/rC/TistK7Gmm8L4WPddCsYdcd+eSnnAG1VQFQXwiG7zn+/+fmnosPYFLWdDsnPx5mXieiS17VkO45bPosNfmVx9kh6IchfvCHnAeQVc3dQrodXqT30KJJNJelqvmKlicoGCdWOqQyjxpKo5vk5ll3VjwMbv9WU8OoW1PBQa17C74ZZLHhbu2rjsT/0ka0maVJ/e2eErIIzvJqZfd6SWLMiv83w93y1z5mC3nGDFKTHXDF6CID+AJ4mbwX6yZBYAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))

whiteKnight       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAw1JREFUWEeVV2taGzEMlK/RbOBAJelZSeiBSjZcw/30tCTLCfgPYdfWYzQaaxv8YDUA6E/3f2+XmsHdD1YDaB2gV0b1aAqJthb7xRQ68yceBFBnYk/Tj5VfAE3C5eliHwEsk2wAvaOZKbH9cuQX0GE77WIrWS/RG8E8LEENMke6X49YG6AMZW2nmwvCAT0lpw+aO21mKrfRAjrXJ7/e/sHXx6ucViT8/jUp8U2JwOoIxnu7bpb54e2THH99vARiHU976yBle9I1HEDyyP8OmAjqBkA1d9upQayfpFuQc9DhcN7xT7k8f+ua+SYVI1zzanke6G8OZjsrJ1KSZRcsoMK9BHsXwmBT0F52xtmkzqZXuTMYRd46RCFyoGDrnWou7iTBjm3ZEGGXsdCJTHR01kjDDh4FCjiFmyodcNgl80hV73TUyjse7elRmKhm9CveNEDnh9+fcP/7YvY0WO1344VkzOFw/RvpFyMx9GGucyiBr8B+2RBns4koTIawM96HJlBpTRE4lkDEyb8XIvHueXJ/P2IOcDzfsJzlCt0RhdH2+8AzzSRmz9DKjzvmft6vHKD2BVMsVjSiNitkqYRPQpDXDe6XrZMmF0FwJChnDQ52R/BOL3R0PCrfYPbQuRG5/lLoRxdpe8UsK9542ZgQmKSgiIfFaSgjtyBnbDTMBEyGfftHxKsI0jPSh8B3Fh0tB26vYZ+zGST05CGHSyzcLCD7Mo6UPQ4o0jvBVFTDkoQentx+Qx0T3zFgZy3UvshFcySpiU7qzI18bgzTy0jEzzG8EK2FjqQAHhOgFB3j3UCEQA5lyAzkOVM70Deni3MuREU+nlWkBS0ddrD94aFkzSar2pNC2DSk93G82kfUWkwlQwcez9ZLJopFjG4M83Cl8cPJ73wZPLsJQxvmOMd1m0TG5J+v2xxcTAdngru05PyRMhqn6GVPOgM1o2z3v8zBDgTmxnoeQJulDigS8yCqzOVjPKsNFPx3ymBBnIqqCdxut/Lb1+OZu+mbGjK1gdlZfhklCX3UR4k4P9hKJ/8DM8yQOdsD3BwAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
whiteKnight_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA85JREFUWEeFV1GWmzAMlK/RhLcHWnLaZA/UAu0t6j5JI3lk2JSfBDC2PBrNyE26dJmuJnJ+aGPizfcj8kMd8vbyOdoIAA+6SC8fN5HuMbbmY+zW/jaRNsdfg9PXNkKHYjn7RKe1H0PgYkcYFLForNe4+EytVShjf77L+mV9R9/Zi9jQjIJhgMkQ3P5csDOR27oR4E2aTmSxAUFDDwvgr/5QCi4SZgtFCirc+2sJDIGAB1FZMu09Uud7QfCKgEF4BusKdM3j9rx71kTkx/pT/rw+PM9d5P7YOOnYFfPENzQC5RSAVKAc1uDcNtlf94Tqtv6y6H+/PvKZEsyQSJKN/DshjY0ZmKXgXdlFjnTMprArcqgU/i5ziRK6r7tDQvnOZRPx4ADnplS7T+uL687HtvSNhh4ly5x1BLt4EHEFGeu9Vc9cKHVnY+coZ9IBwEGB5XrKB60McJcDrYygFCQxSDz2JJzvcQRXYcsStmHj3fK5AyVa9pQCfOOlOrIei/uimACMUVW0Ujdky4ylng0FXKGEfhtyFAhMAqR1riw/rN6ZuYBWRA7lhVGBqz8IjqCUC5/gQo5jZvSmVCoeorGY0GTkTkUllSqc59MXdUEKtk+B9C73x1HlNcwBQ6sZBZQI53guthjDWPCV0IWJD8EhzLM89uquUFhdvEoxp4GdDs8DwWD0kGMKoKBBwdOQJLIBd9EPpD+eDKlab5gRoxLuzGXHRmVEROG7KJ7cMAr3vT8wR7jsRgUqvG1ySVVRiBeQavK3GnZq+KXchq577r+XcMfEuJPQ0+hsaIAA52QYRZRTg7GAWU1EyRmlXJJCeV7WjSqrKAk+DZnv2TSxaqe9ekCwUFhBhb/WRdwtqzI/ywGmVDHTu+TArP+VbqOnOr6WU8PqPV6QSbshkRv1BdGuZf4jMKWbmVEYctERlEAIGpLprhjpITOafOK+HgQNtXKhYZyI/5EpVM+kl7zCfFQ9IRUzSNqN7YaCXtHaXTaol+eCUZ3skNsXy/NQWIfRyRrrZRXwg/BmCliL0mhoOSSJnDlw5Q1wIpwNKGV2ZHACsgy7ZWug7D2+vDeKYPlIHvWAU9fksOLh3FGZhvjDbM1KsYykT16A6LD9ZDzB4UH65KNhq6UYVa8j9EopRqC8/MkLRueqVos+cD7wkTkBPtTAtSaoIqYHjJOeab0HMJ3xwoO0C45d5i/gHTXtdeFc8y8912Bf0zREVzRQG31X8oGBqWwu+zIL9Q4pUsFHpAghQyodE7PLA85zQZYrHSTZjX1D7pS5QxpQlXSw4OpYyhv6B9yAQQN93uZMAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackKnight       = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA0VJREFUWEelV1F24yAMFEfZ2HTvf53E6VXYNyMJBAaavvVPawxoJM1ISpL/fpKIlOUty6/2AX9+8eyM9d/mO++rDcDekQBSN9btfsMsCIs743IfgQ2IlEQKjbRN55ELo5+KXO9rGc0kSXSjP+2OyaENbD9fRPKRSykeiSQpFXmNIGp01p5xCz9/5L3uPY+TpuHX83pKPv+qjyXJ9f1KMUo/EWwRtpDYAVh+nIUGktA48pLPL0kJEJgNeX0jHXtlABj3R4SdrSATjw5ynkrRaJmx0sjR8eMiiJ4z1VrA9hEHGPZHJgdhz9FTDaV5AmD1PSW53i+8Th93dsnceArGcTMPGQpEAmhARGbEw+SpECNlp9fBdT06iKMLKQgHqelB5Lk+AQCXQ0Kj15TncGckabgxEM+sKOHu8tVQJ+OCRqb6Ykz0VapizMPA8WmOYPz5hsS+7DtkpylQqWktgOuUpEWJpDSS0HHpi9SYkSUHoHWaBOvNRxgey0UGOcEPS0GtluRMktdbwQ6Jrq/Lj63gyKTMNhiIFLymPGGy8kHjjjWoYSGGnoSrTat1RAlE4O0hNAZFEBnvEWPk/M6PZDgHkOQ8DppnT9CE0ygv5f96ct+oGDZXWo9zRK3vWm3yn1aStRQYV4wM2htA2LFL3m1UEVW1LOIVl0+TKHuAtaZQE6m8m/HJvS0FnT4shlWAfWvJ6IabAQTZuLXmhQ7uHPiF997HNYWWSuNjAxAaRGSeleEpCWOuxypG3dOIh0CvqKJj6fC5YEbfBQd2xSJ+00lIV1R+sat7NfKZIJBzMR/8OL1EvCw6NIw+oJWO3tdVBYZv2NUVoM7x9rKtA2Ow8uOg79VnSr/1AbZnXSEQLcN2y0IBAcCqVqlXWvWsJXvB6WYAnUxonDzQ4tR6wbzGTGTYswHDCAlHvfsAi+bjR1GNrRfY3zrlzibl7nqP1UBWxxr1rjOFzxaNeArOSy+AtBJMiKXYkDpTxDARxYaC7RxIPM8mNgdhdAvc1jHdCVKV4mloAevM6PIs/ckA2EcddOwXjtcW770uS29IIGIYw3RM30bAph2DP/6QWh2ert/mP98VQhCWNjIcftGFKPm/c93E2Xz7y50w/gHSZNE0hyxWrAAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
blackKnight_green = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABARJREFUWEd1V212wyAMM2cJ2f2vs0GuMvZsyR+Qrn/6moAxsiS7TZYs2T5N5Hy0mkjTZR/e2V48b9KOcE1kLbzWVR6irIsdGdo3cZcmYxv9EE+vrCuH8CgmhOTsjsxD75KfkrKFZ4b1nvux3G3BEBHw7TfdEdXATVoD1Oc5TM+P5HdAldB5nRQIe72aXHePcs05eS6SzIO484jpSZ5Fy+Sj7q/7WAb3ffOF3kyhFBlzvBd7+RxeW6HoAX5LICrxMUsE102OQu8dhFsiP8+3fPUvI5iGm8+HJAIbK1ygpnGtNPYQSRX+nyRElPtS2AHy9/NjB9/3V+5fgiQYLwtvVOBlUGqAs9oq9NjqaFEsEDb0q2e8Egzo6tok2zMeWaa7YEQpL0mSGjkVTiJpagTi7j3h2aDym1DyFIRedY6HiRULoaUsu1QtQTGZU/G9K+GWMd+OMwK5bplXeFVKdc6BklrCy60kSgH7+DXufPiAEF2lRqPBsSkrvQWQTzO1JAv0cwwk7OuKq4YK8vTqByIBe3GPQMDKkzczKYaTuWKaPHO+7Zl3hugcgSrB1aT3S8Yz5L4UfjdzpKrQwgtUEZCWUzkRByH1M8KkeNVyFvEqbkXSmtZRQEqGGi9yVbh1HVSMGi9nbQNn9BIhndBE+l/hgNuws0ksOBxObZYMMD5kqcwXCvOzaXqvaGI88H5Weu1mRLUBnYyEywGMypLLpJnlsWJQKc5rS36n1hY+sSi9Gqwvu7zdBvy4MjhQ9M+JAHkkosYZer+7btKq9oLNL96+jRyR863eEA4IfGs7JxggrBulW4JzgW0ddrdNPG9971IFP6o5bR5Bec5HJYjPXuIkzTEPhKW/jAnOh8dqTnUQ4XmpgrbE5gOWNQ5na05dbVa8Z0mnloVeGVZgCRjzC/XdWMJRW0BPjXJ/6bAMiknJSRNkSymeUPTrjvkg3mn94wcko/D7p8LPphkT0zYRBe+hpgxQfqszptFyHCxd3m+sMwGaTKYWaBREW/tN80qypAQ9Q31i84C9UptFfjFp5fRtzUhJOdiIvBNW0Wwy9CJvwtvGM+qethukCJR0rPJGz7fNE9gn4VMT/w6l6P2kflPZYSbwZl4aJEuVE1Elnqrhn7kINMRMCMhdy26EutEOLg8wDPGwswlRq/hCzGFkhH3hOu6QQGbvhgdpdB7waQU31o6njpfflek+1dpAEhNo9YQPAwzGcmbGsclN5r6uIgV33phGmUi2YFAiCodhdhEF59TBrRzLi+BdA+b3ZZ7xrog+Q1DjYfaJSjRdOgY64mnHH0YytoQsIXsw0379CS1ZF8jPoyBv8L1aOpLyCTLg3/9ko5zxh7CcyCxdDsWG67wTHXPfGb/+AGP3kwnqBM/LAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))

#whiteQueen        = tk.PhotoImage(data = b64decode(""))
#whiteQueen_green  = tk.PhotoImage(data = b64decode(""))
#blackQueen        = tk.PhotoImage(data = b64decode(""))
#blackQueen_green  = tk.PhotoImage(data = b64decode(""))

#whiteKing         = tk.PhotoImage(data = b64decode(""))
#whiteKing_green   = tk.PhotoImage(data = b64decode(""))
#blackKing         = tk.PhotoImage(data = b64decode(""))
#blackKing_green   = tk.PhotoImage(data = b64decode(""))

class CustomButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_green = False
        self.piece = 0
    

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
            if (self.i == eligibleRow and grid[self.i + direction][self.j].piece == 0 and grid[self.i + 2 * direction][self.j].piece == 0):
                grid[self.i + 2 * direction][self.j].config(image = empty_green)
                grid[self.i + 2 * direction][self.j].is_green = True
        except:
            None
        
        try:
            # check if the space in front of it is clear
            if (grid[self.i + direction][self.j].piece == 0):
                grid[self.i + direction][self.j].config(image = empty_green)
                grid[self.i + direction][self.j].is_green = True
        except:
            None
        
        # check for both right and left directions
        for k in [-1, 1]:
            try:
                # check whether the diagonal has an enemy piece
                if (grid[self.i + direction][self.j + k].piece.team != self.team):
                    grid[self.i + direction][self.j + k].config(image = grid[self.i + direction][self.j + k].piece.image_green)
                    grid[self.i + direction][self.j + k].is_green = True
            except:
                None
        
        # en passant
        #if (enPassant == True):
        #    if (self.team == white and self.i == 3):
        #        if (enP)
        #    if (self.team == black and self.i == 4):
                
        
        return
    

class knight(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Knight", team, i, j)
        if (team == white):
            self.image = whiteKnight
            self.image_green = whiteKnight_green
        else:
            self.image = blackKnight
            self.image_green = blackKnight_green
    
    def generateValidMoves(self):
        validMove([-2, -2, 2, 2, -1, 1, -1, 1], [-1, 1, -1, 1, -2, -2, 2, 2])
        return
    

class bishop(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Bishop", team, i, j)
        if (team == white):
            self.image = whiteBishop
            self.image_green = whiteBishop_green
        else:
            self.image = blackBishop
            self.image_green = blackBishop_green
        
    def generateValidMoves(self):
        validMove([1, 1, -1, -1], [1, -1, 1, -1])
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
        validMove([-1, 0, 1, 0], [0, -1, 0, 1])
        return
    

class queen(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Queen", team, i, j)
    

class king(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "King", team, i, j)
    

# Helper function for finding valid moves
def validMove(iMatrix, jMatrix):
    for i in range(len(iMatrix)):
        curI = grid[selected_i][selected_j].piece.i
        curJ = grid[selected_i][selected_j].piece.j
        
        while True:
            try:
                curI += iMatrix[i]
                curJ += jMatrix[i]
                # handle pieces being able to pacman vertically
                if (curI < 0 or curJ < 0):
                    break
                # check if next space is empty
                if (grid[curI][curJ].piece == 0):
                    grid[curI][curJ].config(image = empty_green)
                    grid[curI][curJ].is_green = True
                    if (grid[selected_i][selected_j].piece.pieceType == "Knight" or grid[selected_i][selected_j].piece.pieceType == "King"):
                        break
                    else:
                        continue
                # check if next space is an enemy piece
                if (grid[curI][curJ].piece.team != grid[selected_i][selected_j].piece.team):
                    grid[curI][curJ].config(image = grid[curI][curJ].piece.image_green)
                    grid[curI][curJ].is_green = True
            except:
                None
            break

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
                if (grid[i][j].piece == 0):
                    grid[i][j].config(image = empty)
                else:
                    grid[i][j].config(image = grid[i][j].piece.image)
                grid[i][j].is_green = False
    
    return

def placeNewPiece(piece):
    global grid
    grid[piece.i][piece.j].piece = piece
    grid[piece.i][piece.j].config(image = piece.image)
    return

def movePiece(oldi, oldj, i, j):
    # Define global variables
    global whosTurn, enPassant
    
    grid[i][j].piece = grid[oldi][oldj].piece
    grid[i][j].piece.i = i
    grid[i][j].piece.j = j
    grid[oldi][oldj].piece = 0
    grid[oldi][oldj].config(image = empty)
    
    revert()
    
    if (whosTurn == white):
        whosTurn = black
    else:
        whosTurn = white
    
    if (grid[i][j].piece.pieceType == "Pawn" and abs(oldi - i) == 2):
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
    if (grid[i][j].piece == 0):
        print("empty")
        return
    
    # if selected space has the wrong team
    if (grid[i][j].piece.team != whosTurn):
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
    grid[i][j].piece.generateValidMoves()
    
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
        if i in [1, 6]:
            placeNewPiece(knight(black, 0, i))
            placeNewPiece(knight(white, 7, i))
        if i in [2, 5]:
            placeNewPiece(bishop(black, 0, i))
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
    