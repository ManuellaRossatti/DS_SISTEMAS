import pygame
import random
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def draw_rect(surface, color, position):
    rect = pygame.Rect((position[0] * GRID_SIZE, position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, color, rect)


class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        if new_head in self.positions[1:]:
            return False

        self.positions.insert(0, new_head)
        self.positions.pop()
        return True

    def grow(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def draw(self, surface):
        for position in self.positions:
            draw_rect(surface, GREEN, position)


class Food:
    def __init__(self, snake_positions):
        self.position = self.random_position(snake_positions)

    def random_position(self, snake_positions):
        while True:
            position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if position not in snake_positions:
                return position

    def draw(self, surface):
        draw_rect(surface, RED, self.position)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Jogo da Cobrinha')

    snake = Snake()
    food = Food(snake.positions)
    font = pygame.font.SysFont(None, 36)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        if not snake.move():
            break

        if snake.positions[0] == food.position:
            snake.grow()
            score += 1
            food = Food(snake.positions)

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(f'Pontuação: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

    game_over(screen, font, score)


def game_over(screen, font, score):
    text = font.render('Fim de jogo! Pressione ESC para sair.', True, WHITE)
    score_text = font.render(f'Sua pontuação: {score}', True, WHITE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        screen.blit(text, (20, WINDOW_HEIGHT // 3))
        screen.blit(score_text, (20, WINDOW_HEIGHT // 3 + 40))
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
