#include <iostream>
#include <iomanip>
using namespace std;
int rollDice (){
  return (rand () % 6 + 1);
}
int main (){
  for (int i = 1; i < 101; i++){
      cout << i << " ";
      if (i < 10){
        cout << " ";
	    }
      if (i % 10 == 0){
        cout << "\n";
	    }
  }
  int playerOne = 0;
  int playerTwo = 0;
  const int numWidth = 4;
  const char separator = ' ';
  cout << left << setw (numWidth) << setfill (separator) << "Roll";
  cout << left << setw (numWidth) << setfill (separator) << "Land";
  cout << left << setw (numWidth) << setfill (separator) << "Move";
  cout << left << setw (numWidth) << setfill (separator) << "Roll";
  cout << left << setw (numWidth) << setfill (separator) << "Land";
  cout << left << setw (numWidth) << setfill (separator) << "Move";
  cout << endl;
  while (playerOne < 100 && playerTwo < 100){
      int playerOneDice = rollDice ();
      playerOne = playerOne + playerOneDice;
      int playerTwoDice = rollDice ();
      playerTwo = playerTwo + playerTwoDice;
      cout << "\n";
      //N means nothing special; U means went up a ladder; D means went down a snake. poor child.
      char playerOneM = 'N';
      char playerTwoM = 'N';
      if (playerOne == 3){
        playerOne = 51;
        playerOneM = 'U';
      }
      if (playerOne == 6){
        playerOne = 27;
        playerOneM = 'U';
      }
      if (playerOne == 20){
        playerOne = 70;
        playerOneM = 'U';
	    }
      if (playerOne == 25){
        playerOne = 5;
        playerOneM = 'D';
	    }
      if (playerOne == 34){
        playerOne = 1;
        playerOneM = 'D';
	    }
      if (playerOne == 36){
        playerOne = 55;
        playerOneM = 'U';
	    }
      if (playerOne == 47){
        playerOne = 19;
        playerOneM = 'D';
	    }
      if (playerOne == 63){
        playerOne = 95;
        playerOneM = 'U';
	    }
      if (playerOne == 65){
        playerOne = 52;
        playerOneM = 'D';
	    }
      if (playerOne == 68){
        playerOne = 98;
        playerOneM = 'U';
	    }
      if (playerOne == 87){
        playerOne = 57;
        playerOneM = 'D';
	    }
      if (playerOne == 91){
        playerOne = 61;
        playerOneM = 'D';
      }
      if (playerOne == 99){
        playerOne = 69;
        playerOneM = 'D';
	    }
      if (playerTwo == 3){
        playerTwo = 51;
        playerTwoM = 'D';
	    }
      if (playerTwo == 6){
        playerTwo = 27;
        playerTwoM = 'D';
	    }
      if (playerTwo == 20){
        playerTwo = 70;
        playerTwoM = 'D';
	    }
      if (playerTwo == 25){
        playerTwo = 5;
        playerTwoM = 'D';
	    }
      if (playerTwo == 34){
        playerTwo = 1;
        playerTwoM = 'D';
	    }
      if (playerTwo == 36){
        playerTwo = 55;
        playerTwoM = 'U';
	    }
      if (playerTwo == 47){
        playerTwo = 19;
        playerTwoM = 'D';
	    }
      if (playerTwo == 63){
        playerTwo = 95;
        playerTwoM = 'U';
      }
      if (playerTwo == 65){
        playerTwo = 52;
        playerTwoM = 'D';
	    }
      if (playerTwo == 68){
        playerTwo = 98;
        playerTwoM = 'U';
	    }
      if (playerTwo == 87){
        playerTwo = 57;
        playerTwoM = 'D';
	    }
      if (playerTwo == 91){
        playerTwo = 61;
        playerTwoM = 'D';
	    }
      if (playerTwo == 99){
        playerTwo = 69;
        playerTwoM = 'D';
	    }
      const char separator = ' ';
      const int numWidth = 4;
      cout << left << setw (numWidth) << setfill (separator) << playerOneDice;
      cout << left << setw (numWidth) << setfill (separator) << playerOne;
      cout << left << setw (numWidth) << setfill (separator) << playerOneM;
      cout << left << setw (numWidth) << setfill (separator) << playerTwoDice;
      cout << left << setw (numWidth) << setfill (separator) << playerTwo;
      cout << left << setw (numWidth) << setfill (separator) << playerTwoM;
      cout << endl;
      if (playerOne > 99){
	      cout << "Player One won!";
	    }else if (playerTwo > 99){
	      cout << "Player Two won!";
	    }
    }
  return 0;
}
