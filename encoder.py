https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# encoder.py
# COMP9444, CSE, UNSW

import torch

star16 = torch.Tensor(
    [[1,1,0,0,0,0,0,0],
     [0,1,1,0,0,0,0,0],
     [0,0,1,1,0,0,0,0],
     [0,0,0,1,1,0,0,0],
     [0,0,0,0,1,1,0,0],
     [0,0,0,0,0,1,1,0],
     [0,0,0,0,0,0,1,1],
     [1,0,0,0,0,0,0,1],
     [1,1,0,0,0,0,0,1],
     [1,1,1,0,0,0,0,0],
     [0,1,1,1,0,0,0,0],
     [0,0,1,1,1,0,0,0],
     [0,0,0,1,1,1,0,0],
     [0,0,0,0,1,1,1,0],
     [0,0,0,0,0,1,1,1],
     [1,0,0,0,0,0,1,1]])

# REPLACE heart18 WITH AN 18-by-14 TENSOR
# TO REPRODUCE IMAGE SHOWN IN SPEC
heart18 = torch.Tensor([[0]])

# REPLACE target1 WITH DATA TO PRODUCE
# A NEW IMAGE OF YOUR OWN CREATION
target1 = torch.Tensor([[0]])

# REPLACE target2 WITH DATA TO PRODUCE
# A NEW IMAGE OF YOUR OWN CREATION
target2 = torch.Tensor([[0]])

