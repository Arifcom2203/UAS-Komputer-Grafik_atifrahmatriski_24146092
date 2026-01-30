import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ---------- KUBUS 3D ----------
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

edges = (
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,7),(7,6),(6,4),
    (0,4),(1,5),(2,7),(3,6)
)

def draw_cube():
    glBegin(GL_LINES)
    glColor3f(0.8, 0.8, 0.8)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# ---------- PERSEGI 2D ----------
square = [
    [-0.2, -0.2],
    [ 0.2, -0.2],
    [ 0.2,  0.2],
    [-0.2,  0.2]
]

def draw_square():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for x, y in square:
        glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (900,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("UAS Komputer Grafik")

    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslatef(0, 0, -10)

    cube_pos = [-2, 0, 0]
    square_pos = [2, 0]
    cube_rot = [0, 0, 0]
    cube_scale = 1
    square_rot = 0
    square_scale = 1
    shear = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # Kubus
        if keys[K_w]: cube_pos[1] += 0.05
        if keys[K_s]: cube_pos[1] -= 0.05
        if keys[K_a]: cube_pos[0] -= 0.05
        if keys[K_d]: cube_pos[0] += 0.05
        if keys[K_q]: cube_pos[2] += 0.05
        if keys[K_e]: cube_pos[2] -= 0.05

        if keys[K_i]: cube_rot[0] += 2
        if keys[K_k]: cube_rot[0] -= 2
        if keys[K_j]: cube_rot[1] += 2
        if keys[K_l]: cube_rot[1] -= 2
        if keys[K_u]: cube_rot[2] += 2
        if keys[K_o]: cube_rot[2] -= 2

        if keys[K_EQUALS]: cube_scale += 0.02
        if keys[K_MINUS]: cube_scale -= 0.02

        # Persegi
        if keys[K_UP]: square_pos[1] += 0.05
        if keys[K_DOWN]: square_pos[1] -= 0.05
        if keys[K_LEFT]: square_pos[0] -= 0.05
        if keys[K_RIGHT]: square_pos[0] += 0.05

        if keys[K_r]: square_rot += 2
        if keys[K_t]: square_rot -= 2

        if keys[K_z]: square_scale += 0.02
        if keys[K_x]: square_scale -= 0.02

        if keys[K_h]: shear += 0.02
        if keys[K_y]: shear -= 0.02

        if keys[K_f]:
            for p in square: p[0] *= -1
        if keys[K_g]:
            for p in square: p[1] *= -1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        # Kubus
        glPushMatrix()
        glTranslatef(*cube_pos)
        glScalef(cube_scale, cube_scale, cube_scale)
        glRotatef(cube_rot[0], 1,0,0)
        glRotatef(cube_rot[1], 0,1,0)
        glRotatef(cube_rot[2], 0,0,1)
        draw_cube()
        glPopMatrix()

        # Persegi
        glPushMatrix()
        glTranslatef(square_pos[0], square_pos[1], 0)
        glScalef(square_scale, square_scale, 1)
        glRotatef(square_rot, 0,0,1)
        glMultMatrixf([
            1, shear, 0, 0,
            0,   1,  0, 0,
            0,   0,  1, 0,
            0,   0,  0, 1
        ])
        draw_square()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

main()
