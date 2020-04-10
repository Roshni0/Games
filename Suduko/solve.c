#include<stdio.h>

int suduko[9][9]={
    {2,0,0,5,0,0,1,0,7},
    {0,0,0,9,2,0,0,0,0},
    {0,7,0,4,8,0,2,0,6},
    {4,6,0,3,0,0,0,0,5},
    {0,2,9,0,7,0,8,1,0},
    {7,0,0,0,0,4,0,6,9},
    {9,0,7,0,3,6,0,5,0},
    {0,0,0,0,4,9,0,0,0},
    {6,0,4,0,0,2,0,0,8}
};
int grid[9][9]={
    {2,0,0,5,0,0,1,0,7},
    {0,0,0,9,2,0,0,0,0},
    {0,7,0,4,8,0,2,0,6},
    {4,6,0,3,0,0,0,0,5},
    {0,2,9,0,7,0,8,1,0},
    {7,0,0,0,0,4,0,6,9},
    {9,0,7,0,3,6,0,5,0},
    {0,0,0,0,4,9,0,0,0},
    {6,0,4,0,0,2,0,0,8}
};
int rowPresence(int row, int num)    {
    int col;
    int x=1;
    for(col=0;col<9;col++)
        if(suduko[row][col] == num){
            return 0;
        }    
    return x;
}
int colPresence(int col, int num) {
    int row;
    int x=1;
    for(row=0;row<9;row++)
        if(suduko[row][col]==num){
            return 0;
        }    
    return x;
}
int miniGridPres(int num, int rowCount, int colCount)
{
    int x=1;
    int row;
    int col;
    for(row = rowCount; row < rowCount+3; row++)
        for(col = colCount; col < colCount+3; col++)
            if(suduko[row][col]==num){
                return 0;
            }    
    return x;
}
void printSuduko()
{
    int i,j;
    for(i=0;i<9;i++){ 
        for(j = 0; j < 9; j++){
            printf("%d",suduko[i][j]);
            if(j>7){
                printf("\n");
            } 
        }
    }
}
int main()
{
    int i,j,num,row,col;
    int tracki,trackj,roww,coll,miniGrid;
    for(i = 0; i < 9; i++){
        for(j = 0; j < 9; j++){
            if(suduko[i][j]==0){
                num=1;
                do{
                    if(num>9){
                        tracki=i;
                        if(j==0){
                            if(i!=0){
                                trackj=8;
                                tracki=i-1;
                            }
                        }
                        else{
                            trackj=j-1;
                        }
                        for(i=tracki;i>=0;i--){
                            for(j=trackj;j>=0;j--){
                                trackj=8;
                                if(grid[i][j]==0&&suduko[i][j]==9){
                                    suduko[i][j]=0;
                                }
                                else if(grid[i][j]==0&&suduko[i][j]<9){
                                    num=suduko[i][j]+1;
                                    suduko[i][j]=0;
                                    goto checkWorks;
                                }
                            }
                        }
                    }
                    checkWorks:
                    row=rowPresence(i, num);
                    col=colPresence(j,num);
                    if(j<3){
                        roww=0;
                    }
                    if(j>2 && j<6){
                        roww=3;
                    }
                    if(j>5){
                        roww=6;
                    } 
                    if(i<3){
                        coll=0;
                    }   
                    if(i>2 && i<6){
                        coll=3;
                    }
                    if(i>5){
                        coll=6;
                    }
                    miniGrid=miniGridPres(num,roww,coll);
                    if(row==1&&col==1&&miniGrid==1){
                        suduko[i][j]=num;
                    }else{
                        num++;
                    }
                }
                while(row==0||col==0||miniGrid==0);
            }
        }
    }
    printSuduko();
}
