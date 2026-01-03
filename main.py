import os
import dotenv


def main():
    """Main execution block"""
    try:
        # Load environment variables
        dotenv.load_dotenv()
        print("Hello, AI Brief Bot!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
