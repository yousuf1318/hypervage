
def printTwoElements( self, a):
	for i in range(a):
		if self[abs(self[i])-1] > 0:
			self[abs(self[i])-1] = -self[abs(self[i])-1]
		else:
			print("The repeating element is", abs(self[i]))
			
	for i in range(a):
		if self[i]>0:
			print("and the missing element is", i + 1)

self =[ 873, 854, 355, 178, 157, 730, 97, 264, 376, 129, 721, 361, 298, 734, 797, 905, 570, 811, 289, 415, 120, 295, 100, 575, 895, 554, 810, 537, 47, 388, 770, 702, 643, 510, 197, 649, 500, 751, 596, 755, 871, 217, 456, 26, 567, 200, 571, 578, 93, 365, 114, 484, 657, 875, 620, 223, 110, 498, 35, 597, 740, 73, 565, 331, 845, 861, 725, 160, 343, 808, 61, 453, 743, 428, 242, 299, 358, 278, 434, 535, 460, 637, 209, 229, 586, 327, 172, 102, 585, 249, 256, 795, 658, 13, 161, 706, 450, 219, 594, 146, 470, 798, 720, 443, 850, 830, 62, 558, 192, 712, 448, 576, 214, 250, 45, 767, 257, 713, 336, 817, 87, 269, 305, 538, 849, 497, 346, 483, 841, 882, 411, 869, 339, 822, 121, 781, 136, 455, 568, 540, 247, 198, 679, 398, 206, 610, 324, 372, 403, 858, 70, 676, 27, 150, 42, 236, 439, 354, 891, 884, 1, 412, 99, 123, 878, 901, 334, 639, 673, 754, 707, 78, 632, 143, 107, 436, 176, 115, 897, 363, 353, 714, 292, 508, 828, 271, 349, 287, 142, 653, 820, 521, 216, 819, 672, 226, 663, 527, 396, 463, 492, 844, 881, 645, 11, 163, 898, 762, 25, 446, 829, 581, 678, 782, 531, 812, 856, 642, 48, 518, 577, 465, 623, 451, 742, 266, 598, 757, 908, 855, 831, 723, 906, 475, 221, 340, 909, 345, 665, 711, 836, 386, 438, 799, 19, 168, 328, 718, 778, 660, 557, 218, 57, 479, 329, 175, 551, 588, 818, 695, 317, 76, 326, 153, 384, 211, 769, 691, 309, 561, 335, 185, 262, 49, 801, 792, 414, 622, 719, 842, 8, 480, 516, 30, 603, 501, 505, 108, 58, 539, 564, 789, 145, 761, 133, 90, 238, 880, 857, 86, 506, 119, 903, 44, 64, 397, 900, 111, 382, 95, 41, 167, 686, 654, 371, 733, 833, 59, 408, 67, 75, 459, 696, 109, 6, 807, 34, 338, 332, 224, 442, 468, 683, 137, 427, 195, 685, 559, 429, 193, 507, 259, 399, 546, 560, 39, 661, 584, 786, 134, 55, 583, 16, 627, 258, 293, 390, 866, 170, 911, 633, 81, 401, 693, 274, 630, 208, 731, 165, 860, 816, 261, 204, 670, 747, 494, 418, 694, 260, 879, 53, 310, 404, 472, 666, 381, 52, 246, 835, 330, 477, 628, 241, 135, 717, 234, 33, 84, 207, 32, 166, 671, 101, 739, 296, 722, 362, 675, 441, 784, 138, 698, 716, 748, 569, 4, 640, 794, 2, 774, 174, 89, 745, 482, 373, 215, 312, 391, 380, 267, 608, 684, 634, 159, 104, 601, 466, 846, 413, 83, 532, 321, 284, 726, 753, 839, 787, 239, 600, 430, 85, 548, 728, 885, 599, 20, 72, 664, 352, 530, 852, 88, 464, 194, 476, 282, 746, 69, 189, 43, 486, 359, 703, 452, 680, 421, 907, 124, 370, 130, 533, 624, 668, 619, 253, 356, 3, 17, 604, 614, 859, 457, 125, 473, 357, 777, 806, 394, 188, 796, 173, 467, 71, 65, 454, 213, 625, 709, 618, 662, 7, 503, 669, 752, 682, 607, 288, 407, 432, 667, 318, 574, 652, 779, 222, 768, 515, 469, 763, 409, 840, 155, 674, 286, 775, 587, 790, 402, 374, 31, 230, 422, 566, 502, 615, 803, 10, 534, 128, 513, 307, 651, 525, 699, 868, 771, 127, 865, 91, 38, 80, 117, 758, 131, 708, 543, 732, 621, 656, 910, 847, 834, 613, 383, 605, 46, 888, 837, 9, 220, 367, 105, 659, 5, 832, 144, 853, 838, 611, 872, 635, 522, 648, 202, 701, 304, 378, 517, 759, 437, 512, 351, 756, 474, 876, 772, 243, 103, 419, 899, 646, 433, 248, 700, 244, 205, 511, 360, 12, 182, 212, 710, 314, 210, 681, 490, 162, 243, 252, 379, 255, 867, 275, 268, 116, 552, 864, 609, 302, 582, 151, 148, 393, 612, 800, 737, 350, 626, 478, 440, 322, 689, 154, 821, 793, 273, 629, 196, 281, 245, 760, 572, 395, 203, 589, 301, 514, 724, 705, 741, 606, 147, 729, 447, 544, 815, 21, 285, 595, 152, 765, 791, 279, 496, 750, 491, 290, 235, 489, 139, 523, 874, 92, 316, 647, 325, 426, 240, 337, 890, 79, 809, 736, 592, 904, 406, 270, 306, 300, 814, 77, 563, 893, 191, 333, 616, 63, 499, 251, 94, 40, 183, 431, 843, 98, 788, 870, 715, 547, 573, 141, 638, 156, 400, 529, 444, 54, 29, 509, 231, 228, 199, 655, 303, 804, 313, 294, 186, 74, 461, 650, 392, 780, 389, 641, 738, 783, 233, 181, 96, 825, 232, 528, 344, 776, 827, 889, 562, 366, 51, 863, 177, 896, 892, 132, 593, 37, 887, 417, 697, 462, 149, 545, 341, 644, 308, 106, 692, 24, 579, 315, 364, 424, 416, 410, 526, 493, 602, 237, 851, 164, 445, 56, 735, 813, 555, 744, 60, 68, 190, 112, 488, 265, 487, 348, 471, 36, 277, 553, 704, 902, 504, 179, 883, 28, 184, 375, 347, 727, 113, 122, 749, 805, 280, 187, 449, 254, 66, 423, 886, 227, 617, 773, 323, 420, 590, 377, 519, 542, 320, 826, 297, 541, 894, 556, 690, 591, 118, 126, 180, 272, 291, 495, 877, 22, 385, 549, 687, 524, 485, 764, 848, 785, 766, 481, 435, 368, 550, 520, 319, 387, 536, 425, 802, 862, 23, 342, 405, 677, 82, 14, 225, 18, 169, 580, 369, 631, 636, 276, 171, 688, 158, 311, 283, 824, 263, 823, 458, 50, 140, 15 ]

n = len(self)
printTwoElements(self, n)
