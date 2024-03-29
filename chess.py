import tkinter as tk
from base64 import b64decode
from functools import partial

# Flags
debug_mode = False
isSelected = False
enPassant = False
usedEnPassant = False
checkingIfCheck = False
gameOver = False
isPromotingPawn = False

# Variables
white = "White"
black = "Black"
selected_i = 0
selected_j = 0
whosTurn = white
enPassant_j = 0

# Define tkinter window
window = tk.Tk()

# tkinter window setup
window.grid()
window.title("Chess Python")
window['padx'] = 10
window['pady'] = 10

# Image references (kudos to Seth Glasscock for these)
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

whiteQueen        = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAzdJREFUWEeVV2nW0zAMtK9BUy7E63fYFi5EUziGeaPFWqK4JT+6JLY1Gkkjpbd09dbaoHvrX3lf+d+OOF2OJYerMl2tez2uA2C327M8Z+5ZAFlvlBOwaH9cx+Xr2V/367jAYG8Nv0EX7mMpAOEZ1p6DEjTu6w2binGQgTZGGx324bt+Im6jtc5rCWDFbOdl/vqIAb8B3rFZzpNvP363P7++TziX285nkoee+xxYW7ZgIB7wemyGnwhABBjE358Coo82QejJekz+FpwfJbQuojCIv7gnONjjTP8h+Y7ZOEOwqpj8DMkHdi1+zMTbajipOJfrKUMyhfJ/f2yjewScjyH5MmgCWyZhypMuBJ/FhUrPCsPTYCGQauDKmMpGv8P5gcVscRETVAI5JJ7rViu/VUAVE68JZWi3imIdEKNtmAIYYlUEloLOwkTO42vQPVKsIsJJB2rkuEteW/mTonAa8BGmQ2zo8rXzI9lT5/9koLeOmlZKHfoqF6gHDGzurDUUjkFGKfyrPEpIdH2043mZtNlOhMIRrBwEASLaaS9CIAzFfHRqotpJWZUlNHRmesyKmKK36AErpfsoB/IBrIZ6sQgBu3bFlcGq2E7Xh3DJn0w/6wuDwEVqKPUdOh/tlzpzglTngGfdSZhWgzVikTdxIQ8nUYOkFDXcbu5aM+bUC64979ACrS0pQQ4Cpdh220WfvMEzE1rE74LmXOES5NljVq2UZO4Hx3grKDvwmMoLMD77vSZZOnLZgQUKTmg+tc6qjLgKLRBgBBujPec0ZLhZvESUJCHDQKLOZgHSWcKbC4iLTN7vG6nKNC8xYAw6ExYT0YLVNQMJtdZ/zgEWLzeUzmaU+k9IaD9XZRqSmO/3KwbhRvpPnU11UEQoeahlepgN6+jmLqlNlFeDdu4w7nLesvfyTAcEFxod0/gEK01LjUmz8aMQ4Lmq2jQkRqTP8KuAm5AVKnEDxehOHYsuGXq2d1JfuyLhMs1QuE0PfaLzGWxJ5QlVcrm9RDnUipVlYNcqoUvXS3OXDCI2iohJyY95mM7rQyakkGdxUFkUiaFV+T2Zm4s3Id7retCxr/sXk1RxH4A6cek/d/4Ds++sM9YZJ0kAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
whiteQueen_green  = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA9JJREFUWEeFV22y2zAIlI7RsTM9UNLTJu9A7bPbW0QdPhYWWa/1n8Q2EgiWXdzbaKP94+qtqYH8yjX0Hy/prfMmQ+5bG90sbc316sP26mrpLspGvGZYALoR7Xp+7Ppge3x+6SzD5cB7a2O03ksAspUZRcSjtybxtd7O166Ojtet7e7weN40IHku1/m6te1+tONja/vj8Gjr+eeAeh8SC19m4n5L+sRB5BSZmEok7zUg1E1/3a1kUg4f+eTyxUvkWSqDDGhRNRsRhDve7j/b74/v4W+/f6ppvTIA8q0mvb09IFqh5u6QQSjpZ0BiybfHr/ZHs2Oet7uVJIABw8Xi3t/iq1ZGVgoSdDuHKDbTDKyi0GejbVr72X/up/WODE0dFAVXg9pulhV7LJnofsPpvj2OgHCsDocoA+0rVdUVM2Bk86mO3NOno9/WWa7kfQFfKbbBPM5Lbd37kLNUYil0wyj2VqsAsxopZDQIK4H3UtbQT6CsQ4crGahUYWQB4xUY05HlwPiAXeN/9/JdOfEL8qNQqBWP567spRXSfl6DHcQUwcSpK67sAJ7/1SuG+/naKNWWQ4NOwprvhREFH6UUXDtNrbx/i9WCC31foF9P7mcWWtbTRe1t/fY4Sa44i2YeZdR1CCAQWBGQwV7rBjac6SAwwDVKrbMAHK0K/WhDxu0wgZzD4TDOp2dAcqKKZhdUcRbi7nuiESsxXuYBQ38ICDo4OsKUkVsPN9uP7AKABGBlHsneIBAGURQS6sp43LfKgjNveHrETqT6fxez5AKExleGco/bg5I7aUVOO7WDrsKssOp4y2wNz5gwXsziwMYWN8vxVZRmMULnMI1VWlYLC0oIhkma5IjgbgHMDJCwqXqwmLIqAus8uZRZSgKkGLyf6UfJzKHowZVijTdiBIM22DxAXlZa76+P1+66Zw/QQLocUY3WtBtA1yTHxgNUAm13L8EVNHUiUADSMGJKbF5clWOBDKQZT1XaJKAspFoU4pkkE6XJaSgHiExY6oPMhYb2SWEg7cEzijznSoQBXWDgyQCi+zn4fKbPMqB7jDeMxGZmjM8PG03czucBmn6nT4xsO48IGQVFYB7yOmA6Qp/ogCJfSzo5+TmKZJWpuKaMvwMY+ai5akZpianHHKa7SLN+Htj+SXATFWfVehPBiWlvYi9LfZLaqnHimWd+X+iEs482THyUsWgY6ECfGK0xgmRCkW6kH02KjxnjhZyqkSfxWviCnTPH89Ss6oYxbZEGFhrAKQvrOogu0y9pH8t54olS8KfZHC3LBGrCnRf0z+KWZ8dE+RcI7FUGU2qcUAAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
blackQueen        = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAyJJREFUWEeVVwlywzAIhKc0kvP/77S2k6fQ4ZLR5cPTaZzEkmDZXQgCACAAEN+Uyz9pv+mfrJYN9zjflXesr3AGAgI1ocWHl5SJCGH7rP0+88i6MG89urwWWj8r5lem7bMhIEL+ycTYyXsAKM+kTNuun8k1Aw71q+vLNuCMgRwV+xADTlLHZ4h0AVxVOb8W8ow4lL99hXdapFC8djU0zrKPpX2GwCuTnC5RkrwiIfzuf/BOb0AkmHECUZe0hLsXQFi1WBB+mLxaoRmRlWtfRDQ8dUzCIfTlwyhLJlsmQq8EH8J7EmzfjWN4dBkCF5Vvvs5pkbQVBX5V8q37IccrLkWBGH00iw4fqrfKKRPXPcqLo0FEICLYvxtWtXax2MYtQI854Hr3YE158tb9YKz9sauGAJoHBm+TZc8AyEJTQsnK0PJAnI0D8hewrXod+B2R2AGt2IAuek6b/5QEFpDeb4EPpV68sK3ymCwicDloRGrhAfcJsQJhgEDSHzoSRH2ixO4883pcKYkDEN5b9qI9Ali/u0Zll8NrKq2I26igJ/9AE+UhCUCNUIPnO7KmNNHf2AmNS6PMz3SsfLDTxZDUf/bPWkvwhiVNZDg/XrOXbuwGeLRUBDGjuyZk2N0IMzzCPZ+Lz01HiBqHltvDyRFig4BuGqmvj/oChCUlNjzNmt1PGGD/CWD/WhluwjA3ogkwasV2eMV4FELWUgxRVLfHqDfkwCx4hl+6oIB0dF2dC3z0omYomTqNBDwlzGhZmYa8RlIKzty1j8Ay6KaiFs0GmPnQ2EyTS1oEdF0fnNLmQo9rGECV0YyETdrtWC76r31OCSit2OYD6QNhKnJXnAxHEx9whep5Mv9L5gfrWYaqhDCSBc9VQu7uFmeT+bkPSN1NiPUu2oCKDHlcFzLaiGTB9OVgE9NJyufbEEHNDj5cG431PKesFUKbmOOi24g6KlxtUJ3kWZcgnK+O5xnaSC0SVNZHv1IlHFxWFIKftQ4Z8yz3HQEBeALyXu2Dp9igZOl27D8TzBlsn/KbEvF0Tpgi8KxDuDZv+m9T9Ouznuw7a/yTU/4BI12zNKg84g4AAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))
blackQueen_green  = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAABCFJREFUWEd1V1GW5DgIw2eJs/e/zo6Tq3T2gSTA7tn+6KqkYoyFJMiwz75hZp+ZjfjH73HPL76453/xXD6Ne/mDvkcMrPMPX+W3dI3vw8b4sKf9+D5IQYlkVAbxHCJUS86v5zXtG8Oe9WA9f+95xdoxcIYPmyLW4Nn8Xpwqnohj1lWlNK/b3nfZdU17nicemvO28X32vE8E9utnLbvntPW+xBXI5hYbUoFPAJ/7F6R1m1jZPe92Cia3fwSoz7u2yrRItU+iTlTy1OQB6o3C9wI5Eq2y9udddvOe33c0thIolcalADrL6Rwwr9GRCQmYvwyz+5pFqqKO/fsu+yfQQWqeRMZjZZNDSQIcjCX4UKed7snFKCAr5cQDqb5QRHzmdUdgsPbYMdm0nV4q0ANNDSQtFjaO+pL7vsjmTnuQsZeulyLlKBW4IqK8P3EAaYAwttq30yugs13+MD6A6CHWgwSkoyiqfKHwTSmKSxtJJZn8lEnx00sA4ItISSpK8lybp+uKEdojZOj1LMMQ+2WPCFhacCWkellTf3Y1BUi6KYnOg3ZzjJ/xMYdiCi206oEVOD2Bg7WVaTVIIMXDWRv5urBpxTRBWn95qvrAsHldVAVTCFS0iVha5iEzqsNKOQ2KIGHZ8y+QsknxMZ3+mo4EqIPmhKXPAwcs+NXMGInGpt+9tFsCZ0vaPbyCzNt7gDonjX6YvWuhmwbcPXRvc5IcahJd0YE8oIjo3mhgbj2Ac8HtmPA3j0CTqmf7AdrdbFIIzT06Ot25lFr3Irfkck2lzxJ0stGa1WVRnnLVLEG6l057DAAdnXlPDhQsd5Ohw78aD9BwCt0dR1GHTth6xOZUOxpmQUD1jTwM1OIxYjjJDioNbF6O8pL96CVkclSjjVMYn7JRxCIgQAISzvQGOWELHzxiohWK/PL7IGGXTptgmo+rfp6ABxXb47QtodR/cuEgOOdBNadMoEsQEGtuq6HUBw9Y8Dnj8Zru6GrQU45q1l6ThzKO36IE1bR+q6Goc103J11Jx3UM+AAjiv8GD+Rwf6OeCPg3+bdynPz1mVCTFXo5hhLfTEryNYszYdrwYUypOg0y5dftm+Ql2/h86sU0FOIqA4TURKQxQopl42dL2xEpEh6doAfwAeSLd4S6mzMmWZxKSIccYc0QmLoc82++W93wf1qRz/ibmaRhIJnyQRgBOqR0b7bIh71JyRF/dcNuO/XigQP0sNWm+d7V5g91R2YagwpeUgo/2pCG2k4Wtdbw++AXx69I2muPxfSrkhhfv2QqsVnuONiqj/pnO5b2FI7XAb9YXgeCD0Tt9R4HUip53znHDH93ZH8IDOmMKcSIkwlsryhtuMhRKW0vt2hJqM7nS+qpMvgQkYxUtwTOaW5/RU8yqXP+al1dytV6Gzwb3f8DPmq0CUOl5mMAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))

whiteKing         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAuFJREFUWEeVV9mV2zAMJNuIpaSgxFusnRSUWN42mIf7EElx9bEr88IAGAyhWlaeWkppeeF50I/YO73F1XF2CAGXnezYwPu5I6zb/QWD+NRSSzujRQDwZD943FkJBruul+OxtVrBEBiEUxsC3e6HApl7xRsb759ngUF0sPQiwGGIrvb90KVT+zmXksz3Y2uFowAHbC4NlAqHYQUA5Y6zNNgAHmvY2cDt57/y+ed7cMJz4uRdOrsmrN1oyB4MOUCoFfOO/0sp3379LZ+/f+heAdDzI49F0kxCZaHfGxCONko8JHY1pkLPGx9sAGbGNaO0SMgnLkPZQQpvH69am5Vh/8hYkF0Annihqnni/dyo7lLRae6nzqhgYAABOL941nKOB/XxfuwkbS4LEIWoA9coYMW1cAiIdJ5PAzAgl2HE7jan1z6ADng/dDx3VGh9mIvT8svRdJFfqUTcLqEX0pkmNLo0GNUXdaCf6CBMTtc09KoDYJy1rxashJWbUzM7LhVUWtSb/GAVaA2alt0+jlqqADrvGwmTpQBXjC5UO9AI6IUZruUDbwdBd10HuQoYADUQfFQVp2JTYXygQ74ael9cw4qhCfIjx4XuBZgmAmL4U/KvY4lClBI9iZufkptRIM6Yb0DAHN1nExKKONoqrC7BCZxrpbxAC6T6Gqegp6r9IusBWKVMUz3IWjRXw4SEHVmXYt4PG0AJ6SdXAXMBqsBY4w2OpTUAWIkBKiICEAzsClzHqS0LYPzh8T4QlicOCzRHmNwHhKC6DmkKRKvK2pk5TRza2BOa3AiruUPrRsJYFz82FjhACEh+O8uDGNIP+LvfX1Ak0wdOWwAgOXekOx3L9ShJ53lLRWJX5MAYpJCNdFAafeqGfTuqruoi71fDOyKmwCsszgwoqowPRcfG40UU3bC5kUIKok4KDIx1PtKCODNyD0iDbp8J/M0ga6k8RyWuE7YgJUiajc4X7wXHhtNogc38B5FobjWmwlOdAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
blackKing         = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAyZJREFUWEeVV2123DAIFEdpbPf+12ntTY6ivuFDAgnZ7v7I23gNgmEYEJXhQ6WUOj7E/+4H+er/igGR2lb3erPzDvCinEKz4346fqwcTjf2AR7bzm6uz4XH6q6Wusgi86KGWcoZNnhWy/ElByNlcSrZ+EAyHGMA4osDSAMOD2e4YXT82mslKtfnnBN5dqqYaaKr2idxcMD7tnPaDAX57A25JZsCtP9RglKOr6OivmAGCg3oz89Zju13Ywt+vX5OfmUdwlyMNyQoQjoqJLlL6lTK3+sPB8FtwFxISpLWWjjkPp33I044FEce21EBe0uRY6FSSQh1to6wvli0tWvjRgbrzGgyA7l/HdYERaNhVM5va8cHHgyaksA/Hxr7HwFIuKYS+B6yH1zEhu384Kp1qXnHXJRBediJVmu5fhQBk9Ind0KhTDZzTs4qqIQkZD8S7+n0zpGgBG/MGgdsaij75yB0Prjh4v2jLDc6AHwqk8u0nQ9Wtjch5frhsXRClOSOJBEJYdunq2ur4xs1hAJys0ovSgcZJaGI6IR0nM5CAHOlwQKjnApdCzhjm5iZHC8cPLfhoo/V0OaA9aH54+yfz4wa94Z0QdPUACMZ0mvYQX6jwrNot1F9F9ighDNzM2MOgCsoISxFaIA70oNkfMSdZxVr5O+m49haJML/Zg4KKaVm4f13IYV5UKrbhkLBFiM5FOs9CwwDjOUAG2+jNQyjt14da6PJnSagC2wlMC2X5fQj2hwKrTxxdY5qOOtDTgJn1cRIYaAKQKhc39kiMh4Xh37s207qkIS54INlJ2vDmGmk2UEd8f+JQLJztVQ+QxPT4TqSE5EFCEJMknFbq/1GiMUEY/mNuNo4Xjaeh537XhuHAzC2Sw48GpiLIg/9juC8G95DcLFvwvuiZDYF20VKd0LcCYRzAj3XQmEOnAhi1NURj43E6XVq344qBPN3OIzdHrPF2xEwr9oNKzQagnfCh9sP7gItQ81W7wQSVt8KmZ9aAsPkblNiBBidiZ3i2PqdE7bV2xYPPlcD4KWl33j5uXVGopLDhdjJon6d94lZlpZKd6dgydD5ByactTrcPdbxAAAADmVYSWZNTQAqAAAACAAAAAAAAADSU5MAAAAASUVORK5CYII="))
# only useful for debugging
whiteKing_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA9VJREFUWEeFV1GWEzEMS44B08KBtntaugeCneEYDc+WZSuZAfYDpukkdiRZdnsbbbT86/E0Wq7aUrzRe/fXu33urY34H5tiofuTfBcHjN5s97qv94F3PYhvjiAVN9cqUTwdP26+Z3vbMwckh6DIm5eyJ09/umRvL7xne5CJZSGgSHL+7Wht/7jHUTiMQGxvn3OOEguwMB+iwqQUykRCWehtWHZ+YEF9PO8e0BDwCyibSusYAEVQJWS9v7qTyhwAEREo/pL4OAbBK/PtsQfEcbTJKKgoDdkOpYCE+71KYMPjBhXkdIx2fNw1pkf68vjVfj+/TfkBEV6Kerjmo/dhrM7g+QrhFpYpulWMXx8/2/H8nndzLRDzlZapclIDPTI+Q+64iC72521SNnRdSt8en0XiSU+qRHxJpC7lUzdVXVj53VEOUnIG2e19z0Kr0p731ickDeJZr6FWvfFSkFL/hZaxaCjcHp//vUgfA/KihPurjUmthabYCMsQUt2j/Jyb4Noeb+/hAyHgcsQq3VU/icCZnRK8OiVzP1wLUS3mBe+7b4Ch0TMY7gS3OO8L5TpYdkuK3AoTgXAqeOjRl0fbHgeAXWw9SkocVpUASsSlVizqS4MejhdnKV1SXqYFT3itgr9asRSWOxUhVEMMs0IZMqnSAJcuhbgGzgPECRX5uVSqDrhuSXjtiwgNF7NjcWdogjKZGh1Osn97cycEw0kFxRRZJSkDr3sf0ODhnHd3wOok1YrPl2BTm31AO3gcWsGjEUZSKcSohM1KUG+cNKGnTHYkgpcEIOCEDKDEkHIuSW9MrngE8KEkIJy9L21uAQ0UniYi92dzK9uXB+JllostlxkhU/eBSJqVslS0f4zBLC04EAg1ysxBAHQA0QM5jPC9O21Y/eSSkhKWqW+mIGGnzysKlGmIMIwJnRAi09mwbqvd5GzJoGDp0cCa6c/Dqi3TkAg5qbJWzL8eFaPvYM6IEkyRO91/axazh7NMwb+047gAEph99awDii/EiZkQPn92Vp/kU+3Hx3YOELfCXpxyf9vDXhZLy/mhuPexPFV7omIuQxhQNSD2dQ4BZI5t+aocJ0Qce09g0aIk4oeMhoFUogMZHcbmxlF0XI00RcMU2YUziQ93mG4eCZl6k+8VOWfDvCHac1ZenC9WH71gKZXA1ALj7Pl26yCqsOZ3YuXepJYzcDVzwhzJeDU5zqA33lXY/3peQblAoaZBVgF/nKYJ1Y+U2e1wutn01CAgBakB4JVNzAyK/pBVUM0pKZgVKz+1+SNFZo8MEA0DetA2XChSxEi6mhcl9AcHMmYCTK7gNwAAAA5lWElmTU0AKgAAAAgAAAAAAAAA0lOTAAAAAElFTkSuQmCC"))
blackKing_green   = tk.PhotoImage(data = b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA+JJREFUWEeFVwuW3DAIs88yyfb+x+nGuUrdBxIgO+l22rfziWODJATpbbbZ/vnqrf10+e0+281ui9fsrXUeMVvrvbc57YP9t38WgNwUP/n9fjN2wkJ8jYjP4/TPY1yPUGKdnY31vfVue8gOHkcgYIfZ0jyQl/iTX+YLB08mVhleYzDoyFizjwBiF5wnAfCCHxQX8b5nXoEcvsV9XRvszFr2ChzxjuAB8K4BpWPaZYtnk8ls7TxxeGw0GMT/VdNbm7N1ewO1opBFP8I6RXN8DlMRoiYn1/3dvj5fDBSxXjc0Efx7UCpMgEAhEgHf1g4iA0GCVsF5HH6wiSl37K19j9/t6/MrcxmmhawCpXbnf6dAyZaIH8oPRjqFyNIyWMc1GFtgrHVJ7r0G8ftTAxo5q9DP8xoGHufnlARxoc/ZvApCeMYz0Yz7UfuJPvc0OpOTp4TeRGVlaHfBYyAjcC/Qq2cEs0S1MHkxoijCiKlSLZ9wBBwNrwMIcM5234OfC62V9UQ+zay3PzCnnY3K3K7QDTx0fIMg86vAT/UvWJcm4+SojE0D4HLyEHpGnULsDAHPvooZlnyZBsQzXlx0p5Q+UM0C6ZZKy8lb+7gPlOmVEZkGyrSiDBPVJD0J823FCdOWnt0vDQMwHscB/6I5QQxwNtvUhZhNTErQpV46CmIXCt6qcvMcNyLY8GoiXgXj3my7MmZRSoJ7MxKdrE232ki14YMQoq4c/NnbZW05oFj959lleWfv02Unx//UTgC3IYm+UDPDcybgPsJ/WRDOsxXLQPI4Oi03lpdY3Yz8BhjSMPjTLeuAYl50JvqhD7xlrb+pKyAPE2MSMGcb91impVdPlWYXnGQZWhlZDSsZxYt0Jq5wL3ALRvmNaMFLHYXQAHQoP0rQoFuNSEpuDyRCsCSOEyJ0H/KF2MhKMNs6b1iwS+i1KXnSsixaffK5UcFpCPYfHY8oXBemXlro0/UwBdZfFeGmsywnacX42Ml/HROTT9CQfu+6iwlKxy3F5Y12Nh2KPMdpK71Ug+kl5/x1XrdAcuiUMvSj1B9yJtS2ltZaUIYYvQM+5npclUa5dMYaqWVEV8pNypiONih0x+gBnCwdBf8TGSFYNEKI54rOuBuRTFbhoin4VHqkzJvd9Xw1V/CJJn/LRhONFC093THmBi1Rlv1WhgoT7BalhgpeJnmZjgkhZonseDWUenuWZpgWXk9GT6cL07Ag5BGRIxdHc8xloI+L1HLQnq90zEzAEYknLlg5DEUnIePdoZeRbHs4XZ90ObqkMWGxu+RPD6/up4tDVcerGWKlJnvrm7NxSta5qUrvifRfmeN9CNkqeKYAAAAOZVhJZk1NACoAAAAIAAAAAAAAANJTkwAAAABJRU5ErkJggg=="))

# Class for a custom button that has a flag and an object
class CustomButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_green = False
        self.piece = 0
    
# General class for a chess piece that stores the type, color, and location
class chessPiece:
    def __init__(self, pieceType, team, i, j):
        self.pieceType = pieceType
        self.team = team
        self.i = i 
        self.j = j 
        self.hasMoved = False
    
    def __str__(self):
        return f"{self.team} {self.pieceType}"
    
# Pawn class that has a unique generateValidMoves() function
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
        # Define global variables
        global usedEnPassant
        
        # define direction depending on team
        if (self.team == white):
            direction = -1
            eligibleRow = 6
        else:
            direction = 1
            eligibleRow = 1
        
        # Handle pawns being able to "pacman" vertically
        if (self.i == (eligibleRow + 6 * direction)):
            return
        
        try:
            # check if pawn is eligible for moving two spaces
            if (self.i == eligibleRow and all(grid[self.i + k * direction][self.j].piece == 0 for k in [1, 2]) and willKingBeInCheck(self.i, self.j, self.i + 2 * direction, self.j) == False):
                grid[self.i + 2 * direction][self.j].config(image = empty_green)
                grid[self.i + 2 * direction][self.j].is_green = True
        except:
            None
        
        try:
            # check if the space in front of it is clear
            if (grid[self.i + direction][self.j].piece == 0 and willKingBeInCheck(self.i, self.j, self.i + direction, self.j) == False):
                grid[self.i + direction][self.j].config(image = empty_green)
                grid[self.i + direction][self.j].is_green = True
        except:
            None
        
        # check for both right and left directions
        for k in [-1, 1]:
            # Handle pawns being able to "pacman" horizontally
            if ((self.j + k) < 0):
                continue
            try:
                # check whether the diagonal has an enemy piece
                if (grid[self.i + direction][self.j + k].piece.team != self.team and willKingBeInCheck(self.i, self.j, self.i + direction, self.j + k) == False):
                    grid[self.i + direction][self.j + k].config(image = grid[self.i + direction][self.j + k].piece.image_green)
                    grid[self.i + direction][self.j + k].is_green = True
            except:
                None
        
        # en passant
        for k in [-1, 1]:
            try:
                # if enPassant, piece next to you is enemy, on correct row, enpassant column, and wont put king in check
                if (enPassant == True and grid[self.i][self.j + k].piece.team != self.team and self.i == (eligibleRow + 3 * direction) and (self.j + k) == enPassant_j and willKingBeInCheck(self.i, self.j, self.i + direction, self.j + k) == False):
                    grid[self.i + direction][self.j + k].config(image = empty_green)
                    grid[self.i + direction][self.j + k].is_green = True
                    usedEnPassant = True
            except:
                None
        
        return
    
# Knight class
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
        validMove([-2, -2, 2, 2, -1, 1, -1, 1], [-1, 1, -1, 1, -2, -2, 2, 2], self.i, self.j)
        return
    
# Bishop class
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
        validMove([1, 1, -1, -1], [1, -1, 1, -1], self.i, self.j)
        return
    
# Rook class
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
        validMove([-1, 0, 1, 0], [0, -1, 0, 1], self.i, self.j)
        return
    
# Queen class
class queen(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "Queen", team, i, j)
        if (team == white):
            self.image = whiteQueen
            self.image_green = whiteQueen_green
        else:
            self.image = blackQueen
            self.image_green = blackQueen_green
    
    def generateValidMoves(self):
        validMove([-1, 0, 1, 0, 1, 1, -1, -1], [0, -1, 0, 1, 1, -1, 1, -1], self.i, self.j)
        return
    
# King class
class king(chessPiece):
    def __init__(self, team, i, j):
        chessPiece.__init__(self, "King", team, i, j)
        if (team == white):
            self.image = whiteKing
            self.image_green = whiteKing_green
        else:
            self.image = blackKing
            self.image_green = blackKing_green
    
    def generateValidMoves(self):
        validMove([-1, 0, 1, 0, 1, 1, -1, -1], [0, -1, 0, 1, 1, -1, 1, -1], self.i, self.j)
        
        # Left Castling ( j = 2 )
        try:
            if (self.hasMoved == False and grid[self.i][0].piece.hasMoved == False and all(grid[self.i][self.j - k].piece == 0 for k in [1, 2])):
                if (all(willKingBeInCheck(self.i, self.j, self.i, (self.j - k)) == False for k in [1, 2])):
                    grid[self.i][2].config(image = empty_green)
                    grid[self.i][2].is_green = True
        except:
            None
        
        # Right Castling ( j = 6 )
        try:
            if (self.hasMoved == False and grid[self.i][7].piece.hasMoved == False and all(grid[self.i][self.j + k].piece == 0 for k in [1, 2])):
                if (all(willKingBeInCheck(self.i, self.j, self.i, (self.j + k)) == False for k in [1, 2])):
                    grid[self.i][6].config(image = empty_green)
                    grid[self.i][6].is_green = True
        except:
            None
        
        return
    
# Function that takes two sets of directions and generates valid moves in those directions
def validMove(iMatrix, jMatrix, selI, selJ):
    for i in range(len(iMatrix)):
        curI = selI
        curJ = selJ
        while True:
            try:
                curI += iMatrix[i]
                curJ += jMatrix[i]
                
                # Handle pieces being able to "pacman" vertically
                if (curI < 0 or curJ < 0):
                    break
                
                # Check if next space is empty
                if (grid[curI][curJ].piece == 0):
                    # Check if move will put king in check
                    if (willKingBeInCheck(selI, selJ, curI, curJ) == False):
                        grid[curI][curJ].config(image = empty_green)
                        grid[curI][curJ].is_green = True
                    
                    # Break if selected piece is a knight or king (they can't move more than one space)
                    if (grid[selI][selJ].piece.pieceType in ["Knight", "King"]):
                        break
                    else:
                        continue
                
                # Check if next space is an enemy piece, check if move will put king in check
                if (grid[curI][curJ].piece.team != grid[selI][selJ].piece.team and willKingBeInCheck(selI, selJ, curI, curJ) == False):
                    grid[curI][curJ].config(image = grid[curI][curJ].piece.image_green)
                    grid[curI][curJ].is_green = True
            except:
                None
            break

# Function for backing up currently green squares
def backupGreen():
    # Define global variables
    global greenBackup
    
    greenBackup = [[False]*8 for _ in range(8)]
    
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].is_green == True):
                greenBackup[i][j] = True
    
    revert()
    
    return

# Function for restoring green squares
def restoreGreen():
    revert()
    for i in range(0, 8):
        for j in range(0, 8):
            if (greenBackup[i][j] == True):
                if (grid[i][j].piece == 0):
                    grid[i][j].config(image = empty_green)
                    grid[i][j].is_green = True
                else:
                    grid[i][j].config(image = grid[i][j].piece.image_green)
                    grid[i][j].is_green = True
    
    return

# Function for determining if the king is currently in check (back up green spaces before using)
def isKingInCheck(team):
    # Find matching king
    kingI, kingJ = -1, -1
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].piece != 0 and grid[i][j].piece.pieceType == "King" and grid[i][j].piece.team == team):
                kingI, kingJ = i, j
    
    # Search enemy pieces for targets on the king
    returnVal = False
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].piece != 0 and grid[i][j].piece.team != team):
                grid[i][j].piece.generateValidMoves()
                if (grid[kingI][kingJ].is_green == True):
                    returnVal = True
    
    return returnVal

# Function for testing whether a possible move will put the king in check
def willKingBeInCheck(selI, selJ, destI, destJ):
    # Define global variables
    global checkingIfCheck, isSelected
    
    # Avoid recursiveness
    if (checkingIfCheck == True):
        return False
    
    # Update flags
    checkingIfCheck = True
    
    # Temporarily move piece
    tempPiece = grid[destI][destJ].piece
    grid[destI][destJ].piece = grid[selI][selJ].piece
    grid[selI][selJ].piece = 0
    
    # Back up currently green spaces
    backupGreen()
    
    # Determine if king is in check
    returnVal = isKingInCheck(grid[destI][destJ].piece.team)
    
    # Move piece back
    grid[selI][selJ].piece = grid[destI][destJ].piece
    grid[destI][destJ].piece = tempPiece
    tempPiece = 0
    
    # Restore green spaces
    restoreGreen()
    
    # Update flags
    checkingIfCheck = False
    isSelected = True
    
    return returnVal
    
# Main function for pawn promotion
def pawnPromotion(i, j, team):
    # Define global variables
    global isPromotingPawn, popup
    
    #Only possible in debug mode
    if (team == white and i == 7):
        return
    if (team == black and i == 0):
        return
    
    # Generate pop up window
    popup = tk.Toplevel()
    popup.title("Pawn Promotion")
    popup.geometry("232x58")
    popup.protocol("WM_DELETE_WINDOW", lambda k=0, i=i, j=j, team=team: closewindow(i, j, team))
    
    # Add piece options
    if (team == white):
        newKnight = CustomButton(popup, image = whiteKnight, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Knight"))
        newBishop = CustomButton(popup, image = whiteBishop, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Bishop"))
        newRook = CustomButton(popup, image = whiteRook, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Rook"))
        newQueen = CustomButton(popup, image = whiteQueen, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Queen"))
    else:
        newKnight = CustomButton(popup, image = blackKnight, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Knight"))
        newBishop = CustomButton(popup, image = blackBishop, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Bishop"))
        newRook = CustomButton(popup, image = blackRook, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Rook"))
        newQueen = CustomButton(popup, image = blackQueen, width = 32, height = 32, command = lambda i=i, j=j, team=team: finishPromoting(i, j, team, "Queen"))
    
    newKnight.grid(column = 0, row = 0, padx = 10, pady = 10)
    newBishop.grid(column = 1, row = 0, padx = 10, pady = 10)
    newRook.grid(column = 2, row = 0, padx = 10, pady = 10)
    newQueen.grid(column = 3, row = 0, padx = 10, pady = 10)
    
    # Update flags
    isPromotingPawn = True
    
    return
    
# Function for selecting a pawn promotion
def finishPromoting(i, j, team, pieceType):
    # Define global variables
    global isPromotingPawn
    
    # Create new piece
    if (pieceType == "Knight"):
        placeNewPiece(knight(team, i, j))
    elif (pieceType == "Bishop"):
        placeNewPiece(bishop(team, i, j))
    elif (pieceType == "Rook"):
        placeNewPiece(rook(team, i, j))
    else:
        placeNewPiece(queen(team, i, j))
    
    # Update flags
    grid[i][j].piece.hasMoved = True
    isPromotingPawn = False
    
    # Destroy popup
    popup.destroy()
    
    return
    
# Function for handling player avoiding pawn promotion
def closewindow(i, j, team):
    # Destroy popup
    popup.destroy()
    
    # Restart pawn promotion
    pawnPromotion(i, j, team)
    
    return

# Function for reverting greened spaces to regular
def revert():
    # Define global variables
    global isSelected#, selected_i, selected_j
    
    # Deselect previous selection
    isSelected = False
    
    # Clear all green spaces
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].piece == 0):
                grid[i][j].config(image = empty)
            else:
                grid[i][j].config(image = grid[i][j].piece.image)
            grid[i][j].is_green = False
    
    return

# Function for placing a new piece
def placeNewPiece(piece):
    grid[piece.i][piece.j].piece = piece
    grid[piece.i][piece.j].config(image = piece.image)
    return

# Function for moving a piece
def movePiece(oldi, oldj, i, j):
    # Define global variables
    global whosTurn, enPassant, enPassant_i, enPassant_j, usedEnPassant
    
    # Move piece
    grid[i][j].piece = grid[oldi][oldj].piece
    grid[i][j].piece.i = i
    grid[i][j].piece.j = j
    grid[oldi][oldj].piece = 0
    
    # Kill pawn if en passant is used
    if (usedEnPassant == True):
        if (grid[i][j].piece.team == white):
            grid[i + 1][j].piece = 0
            grid[i + 1][j].config(image = empty)
        if (grid[i][j].piece.team == black):
            grid[i - 1][j].piece = 0
            grid[i - 1][j].config(image = empty)
    
    # Move rook if castling
    if (grid[i][j].piece.pieceType == "King" and grid[i][j].piece.hasMoved == False and abs(oldj - j) > 1):
        if (j == 2):
            grid[i][3].piece = grid[i][0].piece
            grid[i][3].piece.i = i
            grid[i][3].piece.j = 3
            grid[i][3].piece.hasMoved = True
            grid[i][0].piece = 0
        if (j == 6):
            grid[i][5].piece = grid[i][7].piece
            grid[i][5].piece.i = i
            grid[i][5].piece.j = 5
            grid[i][5].piece.hasMoved = True
            grid[i][7].piece = 0
    
    # Update board and flags
    revert()
    updateWhosTurn()
    grid[i][j].piece.hasMoved = True
    
    # Check for game over
    if (canTeamMove(whosTurn) == False):
        if (isKingInCheck(whosTurn) == True):
            gameOverFunction()
        else:
            stalemateFunction()
    revert()
    
    # Pawn promotion handling
    if (i in [0, 7] and grid[i][j].piece.pieceType == "Pawn"):
        pawnPromotion(i, j, grid[i][j].piece.team)
    
    # Detect en passant
    if (grid[i][j].piece.pieceType == "Pawn" and abs(oldi - i) == 2):
        enPassant = True
        enPassant_j = j
        print("En Passant = True, j = " + str(j))
    # Reset en passant
    elif (enPassant == True):
        enPassant = False
        usedEnPassant = False
        print("En Passant = False")
    else:
        None
    
    return

# Function for making a new game
def newGameFunction():
    # Define global variables
    global gameOver, whosTurn
    
    # Destroy all old buttons
    newGameButton.destroy()
    whosTurnLabel.destroy()
    try:
        hackButton.destroy()
        teamButton.destroy()
        for i in range(0, 8):
            iLabels[i].destroy()
            jLabels[i].destroy()
        Labels.destroy()
    except:
        None
    for i in range(0, 8):
        for j in range(0, 8):
            grid[i][j].destroy()
    
    # Generate new game
    generateGame()
    
    # Update flags and variables
    gameOver = False
    whosTurn = black
    updateWhosTurn()
    
    return

# Function for if a stalemate is reached
def stalemateFunction():
    # Define global variables
    global gameOver, newGameButton
    
    # Update whosTurnLabel to show result
    whosTurnLabel.config(text = "Game over! " + whosTurn + " is in stalemate!")
    
    # Update flags
    gameOver = True
    
    # Display New Game button
    newGameButton = tk.Button(window, text = "New Game", command = lambda: newGameFunction())
    newGameButton.grid(column = 3, row = 10, columnspan = 4)
    return

# Function for when the game is over
def gameOverFunction():
    # Define global variables
    global gameOver, newGameButton
    
    # Update whosTurn to show winner
    updateWhosTurn()
    whosTurnLabel.config(text = "Game over! " + whosTurn + " wins!")
    
    # Update flags
    gameOver = True
    
    # Display New Game button
    newGameButton = tk.Button(window, text = "New Game", command = lambda: newGameFunction())
    newGameButton.grid(column = 3, row = 10, columnspan = 4)
    return

# Function for checking if a move is possible
def canTeamMove(team):
    # Generate all valid moves
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].piece != 0 and grid[i][j].piece.team == team):
                grid[i][j].piece.generateValidMoves()
    
    # Look for valid moves
    validMoves = False
    for i in range(0, 8):
        for j in range(0, 8):
            if (grid[i][j].is_green == True):
                validMoves = True
    
    return validMoves

# Function for updating a label that shows who's turn it is
def updateWhosTurn():
    # Define global variables
    global whosTurn
    
    # Switch who's turn it is
    if (whosTurn == white):
        whosTurn = black
    else:
        whosTurn = white
    whosTurnLabel.config(text = whosTurn + "'s Turn")
    return

# Function for left click on button
def left(i, j):
    # Define global variables
    global isSelected, selected_i, selected_j
    
    if (gameOver == True or isPromotingPawn == True):
        return
    
    # if selected space is green
    if (grid[i][j].is_green == True):
        # Forcing a piece to place on itself is how I delete a piece while debugging
        if (debug_mode == True and selected_i == i and selected_j == j):
            grid[i][j].piece = 0
            revert()
            return
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
    
    # deselect if selected space is the selected piece
    if (isSelected == True and i == selected_i and j == selected_j):
        revert()
        return
    
    # if a piece is already selected, hide previous valid moves
    #if (isSelected == True):
    revert()
    
    # select current square
    isSelected = True
    selected_i = i
    selected_j = j
    if (debug_mode == True):
        print("selected", i, j, "type", grid[i][j].piece.pieceType)
    
    # generate valid moves
    grid[i][j].piece.generateValidMoves()
    
    return

# Function for right click on button (unused)
def right(i, j):
    print("right,", i, j)
    return

# Function for generating a new game
def generateGame():
    # Define global variables
    global grid, whosTurnLabel, hackButton, teamButton
    
    # Define variables
    grid = [[0]*8 for _ in range(8)]
    iLabels = [0 for _ in range(8)]
    jLabels = [0 for _ in range(8)]
    k = 0
    
    # Generate grid of custom buttons
    for i in range(0, 8):
        for j in range(0, 8):
            grid[i][j] = CustomButton(window, image = empty, width = 32, height = 32, command = None)
            grid[i][j].grid(column = j+1, row = i+1)
            grid[i][j].bind('<Button-1>', lambda k=k, i=i, j=j: left(i, j))
            grid[i][j].bind('<Button-3>', lambda k=k, i=i, j=j: right(i, j))
            if ((i + j) % 2 == 1):
                grid[i][j].config(bg = 'brown')
    
    # Generate debug tools
    if (debug_mode == True):
        for i in range(0, 8):
            iLabels[i] = tk.Label(window, text = str(i))
            iLabels[i].grid(row = i + 1, column = 0)
            jLabels[i] = tk.Label(window, text = str(i))
            jLabels[i].grid(row = 0, column = i + 1)
        Labels = tk.Label(window, text = "i \ j")
        Labels.grid(row = 0, column = 0)
        hackButton = tk.Button(window, text = "hack selected piece", command = lambda: hack())
        hackButton.grid(column = 9, row = 0, rowspan = 2)
        teamButton = tk.Button(window, text = "change whos turn", command = lambda: updateWhosTurn())
        teamButton.grid(column = 9, row = 2, rowspan = 2)
    
    # Place pieces
    for j in range(0, 8):
        placeNewPiece(pawn(black, 1, j))
        placeNewPiece(pawn(white, 6, j))
        if j in [0, 7]:
            placeNewPiece(rook(black, 0, j))
            placeNewPiece(rook(white, 7, j))
        if j in [1, 6]:
            placeNewPiece(knight(black, 0, j))
            placeNewPiece(knight(white, 7, j))
        if j in [2, 5]:
            placeNewPiece(bishop(black, 0, j))
            placeNewPiece(bishop(white, 7, j))
        if j in [3]:
            placeNewPiece(queen(black, 0, j))
            placeNewPiece(queen(white, 7, j))
        if j in [4]:
            placeNewPiece(king(black, 0, j))
            placeNewPiece(king(white, 7, j))
    
    # Load who's turn label
    whosTurnLabel = tk.Label(window, text = "White's Turn", font = ("Segoe UI Variable Text", 13))
    whosTurnLabel.grid(column = 1, row = 9, columnspan = 8)
    
    return

# Function for debug hacking pieces
def hack():
    print("isSelected:", isSelected)
    if (isSelected == True):
        for i in range(0, 8):
            for j in range(0, 8):
                grid[i][j].is_green = True
    return

# main function
generateGame()

window.mainloop()