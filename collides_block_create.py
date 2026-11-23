from blocks import Block


def create_blocks_first_room(blocks, screen):
    block1 = Block(screen, (0, 340, 94, 145))  # left wall
    block2 = Block(screen, (90, 190, 5, 170))
    block3 = Block(screen, (512, 375, 96, 113))
    block4 = Block(screen, (84, 190, 162, 70))

    block5 = Block(screen, (236, 237, 10, 55))

    block6 = Block(screen, (90, 300, 145, 20))  # left gorizont
    block7 = Block(screen, (200, 333, 20, 105))  # left stairs
    block29 = Block(screen, (220, 333, 10, 50))  # left stairs small

    block8 = Block(screen, (361, 190, 161, 70))  # perila left
    block9 = Block(screen, (512, 190, 5, 170))  # perila right

    block11 = Block(screen, (361, 237, 10, 55))

    block12 = Block(screen, (375, 290, 138, 20))  # right gorizont
    block13 = Block(screen, (390, 333, 20, 105))  # right stairs
    block30 = Block(screen, (380, 333, 12, 50))  # right stairs small

    block14 = Block(screen, (0, 46, 72, 10))  # upper stripe small
    block15 = Block(screen, (152, 46, 475, 10))  # upper stripe small

    block16 = Block(screen, (0, 609, 255, 42))
    block17 = Block(screen, (255, 641, 97, 10))
    block18 = Block(screen, (352, 609, 255, 42))
    block19 = Block(screen, (0, 46, 55, 30))  # upper stripe big1
    block20 = Block(screen, (167, 46, 115, 30))  # upper stripe big2
    block21 = Block(screen, (395, 46, 215, 30))  # upper stripe big3

    # tables objects first level
    block22 = Block(screen, (70, 236, 20, 40))  # left up
    block23 = Block(screen, (517, 236, 20, 40))  # right up
    block24 = Block(screen, (94, 401, 20, 40))  # left low
    block25 = Block(screen, (493, 401, 20, 40))  # right low

    block26 = Block(screen, (231, 292, 10, 43))

    block27 = Block(screen, (366, 292, 10, 43))
    block28 = Block(screen, (0, 489, 17 ,15 ))

    block31 = Block(screen, (540, 484, 17, 15))
    block32 = Block(screen, (555, 525, 10, 80))

    colona1 = Block(screen, (232, 500, 17, 15))
    colona2 = Block(screen, (360, 500, 17, 15))


    blocks.add(block1)
    blocks.add(block2)
    blocks.add(block3)
    blocks.add(block4)
    blocks.add(block5)
    blocks.add(block6)
    blocks.add(block7)
    blocks.add(block8)
    blocks.add(block28)

    blocks.add(block8)
    blocks.add(block9)

    blocks.add(block11)
    blocks.add(block12)
    blocks.add(block13)
    blocks.add(block29)

    blocks.add(block14)
    blocks.add(block15)

    blocks.add(block16)
    blocks.add(block17)
    blocks.add(block18)
    blocks.add(block19)
    blocks.add(block20)
    blocks.add(block21)

    blocks.add(block22)
    blocks.add(block23)
    blocks.add(block24)
    blocks.add(block25)

    blocks.add(block26)
    blocks.add(block27)
    blocks.add(block28)
    blocks.add(block29)
    blocks.add(block30)
    blocks.add(block31)
    blocks.add(block32)

    blocks.add(colona1)
    blocks.add(colona2)

    # blocks.add(testportal)


def create_blocks_second_room(blocks, screen):
    block1 = Block(screen, (28, 0, 5, 640))
    block2 = Block(screen, (126, 200, 5, 330))
    block3 = Block(screen, (27, 493, 103, 65))
    block4 = Block(screen, (188, 196, 5, 118))
    block5 = Block(screen, (108, 0, 5, 90))

    block6 = Block(screen, (577, 0, 5, 640))
    block7 = Block(screen, (476, 200, 5, 330))
    block8 = Block(screen, (477, 493, 103, 65))
    block9 = Block(screen, (416, 196, 5, 118))
    block10 = Block(screen, (498, 0, 5, 90))

    block11 = Block(screen, (188, 196, 232, 60))
    block12 = Block(screen, (108, 0, 392, 100))
    block13 = Block(screen, (28, 632, 554, 5))

    block14 = Block(screen, (112, 300, 18, 24))
    block15 = Block(screen, (477, 300, 20, 24))

    block16 = Block(screen, (131, 383, 23, 24))
    block17 = Block(screen, (131, 492, 23, 24))

    block18 = Block(screen, (456, 383, 20, 24))
    block19 = Block(screen, (456, 492, 20, 24))

    block20 = Block(screen, (94, 22, 14, 26))
    block21 = Block(screen, (30, 315, 16, 8))

    block22 = Block(screen, (503, 22, 14, 26))
    block23 = Block(screen, (563, 315, 16, 8))
    block24 = Block(screen, (287, 380, 40, 60))

    blocks.add(block1)
    blocks.add(block2)
    blocks.add(block3)  # left side
    blocks.add(block4)
    blocks.add(block5)

    blocks.add(block6)
    blocks.add(block7)
    blocks.add(block8)  # right side
    blocks.add(block9)
    blocks.add(block10)

    blocks.add(block11)
    blocks.add(block12)  # middle side
    blocks.add(block13)

    blocks.add(block14)  # table left side
    blocks.add(block15)  # table right side

    blocks.add(block16)  # table middle left side
    blocks.add(block17)  # table middle left side

    blocks.add(block18)  # table middle right side
    blocks.add(block19)  # table middle right side

    blocks.add(block20)  # left up flowerpot
    blocks.add(block21)  # left down flowerpot

    blocks.add(block22)  # right up flowerpot
    blocks.add(block23)  # right down flowerpot
    blocks.add(block24)




def create_blocks_third_room(blocks, screen):
    block1 = Block(screen, (0, 126, 452, 12))
    block2 = Block(screen, (354, 126, 257, 12))

    block3 = Block(screen, (192, 126, 40, 25))
    block4 = Block(screen, (379, 126, 40, 25))

    block5 = Block(screen, (0, 126, 110, 72))
    block6 = Block(screen, (510, 126, 110, 72))

    block7 = Block(screen, (0, 346, 40, 82))
    block8 = Block(screen, (568, 346, 40, 82))
    block9 = Block(screen, (0, 546, 40, 82))
    block10 = Block(screen, (568, 546, 40, 82))



    blocks.add(block1)
    blocks.add(block2)

    blocks.add(block3)
    blocks.add(block4)

    blocks.add(block5)
    blocks.add(block6)

    blocks.add(block7)
    blocks.add(block8)

    blocks.add(block9)
    blocks.add(block10)

def create_blocks_fourst_room(blocks, screen):
    block1 = Block(screen, (70, 220, 470, 290))

    blocks.add(block1)











