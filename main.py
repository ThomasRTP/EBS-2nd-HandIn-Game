def on_up_pressed():
    MrPoopyButthole.set_image(img("""
        . . . . . . c c c . . . . . . . 
                . . . . . . c 5 b c . . . . . . 
                . . . . c c c 5 5 c c c . . . . 
                . . c c c c 5 5 5 5 c b c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . c 5 5 5 b b b b 5 5 5 f . . 
                . . f f 5 5 5 5 5 5 5 5 f f . . 
                . . f f f f f f f f f f f f . . 
                . . f f f f f f f f f f f f . . 
                . . . f f f f f f f f f f . . . 
                . . . e e f f f f f f f e . . . 
                . . e b f b 5 b b 5 b c b e . . 
                . . e e f 5 5 5 5 5 5 f e e . . 
                . . . . c b 5 5 5 5 b c . . . . 
                . . . . . f f f f f f . . . . .
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    global SwordSwung
    SwordSwung = True
    MrPoopyButthole.set_image(img("""
        . . . . . . c c c . . . . . . . 
                . . . . . . c 5 b c . . . . . . 
                . . . . c c c 5 5 c c c . . . . 
                . . c c c c 5 5 5 5 c b c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . c 5 5 5 b b b b 5 5 5 f . . 
                . . f f 5 5 5 5 5 5 5 5 f f . . 
                . . f f f b f e e f b f f f . . 
                . . f f f 1 f b b f 1 f f f . . 
                . . . f f b b b b b b f f . . . 
                . . . e e f e e e e f e e . 1 1 
                . . e b f b 5 b b 5 b c b e 9 9 
                . . e e f 5 5 5 5 5 5 f e e 9 9 
                . . . . c b 5 5 5 5 b c . . 1 1 
                . . . . . f f f f f f . . . . .
    """))
    pause(500)
    MrPoopyButthole.set_image(img("""
        . . . . . . c c c . . . . . . . 
                . . . . . . c 5 b c . . . . . . 
                . . . . c c c 5 5 c c c . . . . 
                . . c c c c 5 5 5 5 c b c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . c 5 5 5 b b b b 5 5 5 f . . 
                . . f f 5 5 5 5 5 5 5 5 f f . . 
                . . f f f b f e e f b f f f . . 
                . . f f f 1 f b b f 1 f f f . . 
                . . . f f b b b b b b f f . . . 
                . . . e e f e e e e f e e . . . 
                . . e b f b 5 b b 5 b c b e . . 
                . . e e f 5 5 5 5 5 5 f e e . . 
                . . . . c b 5 5 5 5 b c . . . . 
                . . . . . f f f f f f . . . . .
    """))
    SwordSwung = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    MrPoopyButthole.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . c c . . . . . . . 
                . . . . . . c c 5 c . . . . . . 
                . . . . c c 5 5 5 c c c . . . . 
                . . c c c c 5 5 5 5 c b c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . c 5 5 5 b b b b 5 5 5 f . . 
                . . . f 5 5 5 5 5 5 5 5 f f . . 
                . . . . f e e e f b e e f f . . 
                . . . . f e b b f 1 b f f f . . 
                . . . . f b b b b e e f f . . . 
                . . . . . f e e e b b e f . . . 
                . . . . f 5 b b e b b e . . . . 
                . . . . c 5 5 5 5 e e f . . . . 
                . . . . . f f f f f f . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite, location):
    global currentLevel
    if True:
        currentLevel += 1
        changeLevel(currentLevel)
        scene.camera_shake(4, 500)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_west,
    on_overlap_tile)

def changeLevel(levelNum: number):
    global _1stEnemy, _2ndEnemy, _3rdEnemy
    if levelNum == 0:
        tiles.set_tilemap(tilemap("""
            Prøve lvl 1
        """))
        scene.set_background_color(13)
        tiles.place_on_random_tile(MrPoopyButthole, sprites.builtin.forest_tiles8)
        for index in range(4):
            _1stEnemy = sprites.create(img("""
                    ......ffff..............
                                    ....fff22fff............
                                    ...fff2222fff...........
                                    ..fffeeeeeefff..........
                                    ..ffe222222eef..........
                                    ..fe2ffffff2ef..........
                                    ..ffffeeeeffff......ccc.
                                    .ffefbf44fbfeff....cddc.
                                    .ffefbf44fbfeff...cddc..
                                    .fee4dddddd4eef.ccddc...
                                    fdfeeddddd4eeffecddc....
                                    fbffee4444ee4fddccc.....
                                    fbf4f222222f1edde.......
                                    fcf.f222222f44ee........
                                    .ff.f445544f............
                                    ....ffffffff............
                                    .....ff..ff.............
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            _1stEnemy.set_position(randint(20, 232), randint(20, 232))
            _1stEnemy.follow(MrPoopyButthole, 20)
    elif levelNum == 1:
        for index2 in range(4):
            _1stEnemy.destroy(effects.ashes, 200)
        for index3 in range(4):
            _2ndEnemy = sprites.create(img("""
                    ........................
                                    ........................
                                    ........................
                                    ..........ffff..........
                                    ........ff1111ff........
                                    .......fb111111bf.......
                                    .......f1111111dbf......
                                    ......fd1111111ddf......
                                    ......fd111111dddf......
                                    ......fd111ddddddf......
                                    ......fd111ddddddf......
                                    ......fd1dddddddbf......
                                    ......fd1dfbddbbff......
                                    ......fbddfcdbbcf.......
                                    .....ffffccddbfff.......
                                    ....fcb1bbbfcffff.......
                                    ....f1b1dcffffffff......
                                    ....fdfdf..ffffffffff...
                                    .....f.f.....ffffff.....
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            _2ndEnemy.set_position(randint(20, 232), randint(20, 232))
            _2ndEnemy.follow(MrPoopyButthole, 20)
        tiles.set_tilemap(tilemap("""
            level2
        """))
        tiles.place_on_random_tile(MrPoopyButthole, sprites.dungeon.dark_ground_north_west0)
    elif levelNum == 2:
        for index4 in range(4):
            _2ndEnemy.destroy(effects.ashes, 500)
        for index5 in range(4):
            _3rdEnemy = sprites.create(img("""
                    . . f f f . . . . . . . . f f f 
                                    . f f c c . . . . . . f c b b c 
                                    f f c c . . . . . . f c b b c . 
                                    f c f c . . . . . . f b c c c . 
                                    f f f c c . c c . f c b b c c . 
                                    f f c 3 c c 3 c c f b c b b c . 
                                    f f b 3 b c 3 b c f b c c b c . 
                                    . c 1 b b b 1 b c b b c c c . . 
                                    . c 1 b b b 1 b b c c c c . . . 
                                    c b b b b b b b b b c c . . . . 
                                    c b 1 f f 1 c b b b b f . . . . 
                                    f f 1 f f 1 f b b b b f c . . . 
                                    f f 2 2 2 2 f b b b b f c c . . 
                                    . f 2 2 2 2 b b b b c f . . . . 
                                    . . f b b b b b b c f . . . . . 
                                    . . . f f f f f f f . . . . . .
                """),
                SpriteKind.enemy)
            _3rdEnemy.set_position(randint(20, 232), randint(20, 232))
            _3rdEnemy.follow(MrPoopyButthole, 20)
        tiles.set_tilemap(tilemap("""
            level3
        """))
        tiles.place_on_random_tile(MrPoopyButthole, sprites.dungeon.floor_light4)

def on_right_pressed():
    MrPoopyButthole.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . c c . . . . . . . 
                . . . . . . c 5 c c . . . . . . 
                . . . . c c c 5 5 5 c c . . . . 
                . . c c b c 5 5 5 5 c c c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . f 5 5 5 b b b b 5 5 5 c . . 
                . . f f 5 5 5 5 5 5 5 5 f . . . 
                . . f f e e b f e e e f . . . . 
                . . f f f b 1 f b b e f . . . . 
                . . . f f e e b b b b f . . . . 
                . . . f e b b e e e f . . . . . 
                . . . . e b b e b b 5 f . . . . 
                . . . . f e e 5 5 5 5 c . . . . 
                . . . . . f f f f f f . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    MrPoopyButthole.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . c c . . . . . . 
                . . . . . . . c 5 c . . . . . . 
                . . . . c c c 5 5 c c c . . . . 
                . . c c b c 5 5 5 5 c c c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . f 5 5 5 b b b b 5 5 5 c . . 
                . . f f 5 5 5 5 5 5 5 5 f f . . 
                . . f f f b f e e f b f f f . . 
                . . f f f 1 f b b f 1 f f f . . 
                . . . f e e e b b b b f f . . . 
                . . . e b b e e e e f b b e . . 
                . . . e b b e b b 5 5 f e e . . 
                . . . . c e e 5 5 5 5 5 f . . . 
                . . . . . f f f f f f f . . . .
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.over(False, effects.melt)
info.on_life_zero(on_life_zero)

def on_on_overlap(sprite2, otherSprite):
    if SwordSwung == True:
        otherSprite.destroy(effects.ashes, 200)
        info.change_score_by(1)
    elif False:
        pass
    else:
        info.change_life_by(-1)
        otherSprite.destroy(effects.ashes, 200)
        info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

_3rdEnemy: Sprite = None
_2ndEnemy: Sprite = None
_1stEnemy: Sprite = None
SwordSwung = False
currentLevel = 0
MrPoopyButthole: Sprite = None
info.set_life(3)
info.set_score(0)
MrPoopyButthole = sprites.create(img("""
        . . . . . . c c c . . . . . . . 
            . . . . . . c 5 b c . . . . . . 
            . . . . c c c 5 5 c c c . . . . 
            . . c c c c 5 5 5 5 c b c c . . 
            . c b b 5 b 5 5 5 5 b 5 b b c . 
            . c b 5 5 b b 5 5 b b 5 5 b c . 
            . . c 5 5 5 b b b b 5 5 5 f . . 
            . . f f 5 5 5 5 5 5 5 5 f f . . 
            . . f f f b f e e f b f f f . . 
            . . f f f 1 f b b f 1 f f f . . 
            . . . f f b b b b b b f f . . . 
            . . . e e f e e e e f e e . . . 
            . . e b f b 5 b b 5 b c b e . . 
            . . e e f 5 5 5 5 5 5 f e e . . 
            . . . . c b 5 5 5 5 b c . . . . 
            . . . . . f f f f f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(MrPoopyButthole)
currentLevel = 0
changeLevel(0)
scene.camera_follow_sprite(MrPoopyButthole)