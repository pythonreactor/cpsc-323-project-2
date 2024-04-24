import settings
from syntax_analyzer import SyntaxAnalyzer
from utils import print_analyzer_welcome_banner

logger = settings.getLogger(__name__)


def main():
    print_analyzer_welcome_banner()

    analyzer = SyntaxAnalyzer()
    analyzer.run()


if __name__ == '__main__':
    main()
