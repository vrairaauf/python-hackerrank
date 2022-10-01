class hackerRank:
    def libraryFine(self, d1, m1, y1, d2, m2, y2)->int:
        if y1>y2:
            return 10000
        elif m1>m1 and y1==y2:
            return 500*(m1-m2)
        elif d1>d2 and m1==m2 and y1==y2:
            return 15*(d1-d2)
        else:
            return 0
	##############################
    def equalizeArray(self,arr:list)->int:
        mostRepeated:int 
        mostRepeated=0
        for n in arr:
            rep=0
            for i in arr:
                if n==i:
                    rep+=1
            if rep>mostRepeated:
                mostRepeated=rep
        return len(arr)-mostRepeated
    ###########################
    def cutTheStick(self, arr:list)->list:
        sizes=[]
        cmpt=0
        while(len(arr)!=0):
            sizes.append(len(arr))
            minimum=min(arr)
            index=0
            for number in arr:
                if number==minimum:
                    arr.remove(minimum)
                index+=1
            index=0
            for item in arr:
                arr[index]=arr[index]-minimum
            cmpt+=1
        return sizes
	#################################
	
    def leftRotate(self, d:int, arr:list)->list:
        result=[]
        for cmpt in range(len(arr)):
            result.append(arr[(cmpt+d)%len(arr)]);
        return result
        
    ###########################
    def matchingString(self, stringList:list, queries:list)->list:
        response=[]
        for ch in queries:
            count=0
            for sch in stringList:
                if ch==sch:
                    count+=1
            response.append(count)
        return response
    ###########################

hack=hackerRank()
#print(hack.libraryFine(17, 1, 1999, 11, 1, 1999))
#print(hack.cutTheStick([1,2,3, 4]))
#print(hack.equalizeArray([1, 2, 3, 3]))
#print(hack.leftRotate(2, [1,2,3,4,5]))
#print(hack.matchingString(["ab", "ab", "abc"], ["ab", "abc", "ac"]))
"""

class Result {

    /*
     * Complete the 'queensAttack' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER k
     *  3. INTEGER r_q
     *  4. INTEGER c_q
     *  5. 2D_INTEGER_ARRAY obstacles
     */

    public static int queensAttack(int n, int k, int r_q, int c_q, List<List<Integer>> obstacles) {
    // Write your code here
        int possibleAttacks=0;
        /*
        int rightD=n-c_q;
        int leftD=c_q-1;
        
        int topD=n-r_q;
        int bottomD=r_q-1;
        
        
        if(rightD>0){
            possibleAttacks+=rightD;
        }if(leftD>0){
            possibleAttacks+=leftD;
        }
        if(topD>0){
            possibleAttacks+=topD;
        }
        if(bottomD>0){
            possibleAttacks+=bottomD;
        }
        */
        possibleAttacks+=numberOfColDiagonalTop(n, r_q, c_q, obstacles);
        possibleAttacks+=numberOfColDiagonalBottom(n, r_q, c_q, obstacles);
        possibleAttacks+=numberOfColDiagonalLeft(n, r_q, c_q, obstacles);
        possibleAttacks+=numberOfColDiagonalRight(n, r_q, c_q, obstacles);
        
        possibleAttacks+=numberOfColDiagonalLeftTop(n, r_q, c_q, obstacles);
        possibleAttacks+=numberOfColDiagonalRightTop(n, r_q, c_q, obstacles);
        possibleAttacks+=numberOfColDiagonalLeftBottom(n, r_q, c_q, obstacles);
        possibleAttacks+=numberOfColDiagonalRightBottom(n, r_q, c_q, obstacles);
        return possibleAttacks;
    }
    /*---------------------------------------*/
    public static boolean searchInTwoDArray(List<List<Integer>> arr, int n1, int n2){
        for(List<Integer> sousArr:arr){
            if(sousArr.get(0)==n1 && sousArr.get(1)==n2)
                return true;
        }
        return false;
    }
    /*---------------------------------------*/
    public static int numberOfColDiagonalLeftTop(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q+1;
        int startCol=c_q-1;
        int res=0;
        while(startRow<=dimensions && startCol>0){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startRow++;
            startCol--;
        }
        
        return res;
    }
     public static int numberOfColDiagonalRightTop(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q+1;
        int startCol=c_q+1;
        int res=0;
        while(startRow<=dimensions && startCol<=dimensions){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startRow++;
            startCol++;
        }
        
        return res;
    }
    
    /*-------------------------*/
     public static int numberOfColDiagonalLeftBottom(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q-1;
        int startCol=c_q-1;
        int res=0;
        while(startRow>0 && startCol>0){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startRow--;
            startCol--;
        }
        
        return res;
    }
    /*--------------------------*/
     public static int numberOfColDiagonalRightBottom(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q-1;
        int startCol=c_q+1;
        int res=0;
        while(startRow>0 && startCol<=dimensions){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startRow--;
            startCol++;
        }
        
        return res;
    }
    /*search in top*/
    
    public static int numberOfColDiagonalTop(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q+1;
        int startCol=c_q;
        int res=0;
        while(startRow<=dimensions){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startRow++;
        }
        
        return res;
    }
    
    /*------------search in bottom--------*/
   public static int numberOfColDiagonalBottom(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q-1;
        int startCol=c_q;
        int res=0;
        while(startRow>0){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startRow--;
        }
        
        return res;
    }
    /*----------------------search in lef --------------*/
       public static int numberOfColDiagonalLeft(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q;
        int startCol=c_q-1;
        int res=0;
        while(startCol>0){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startCol--;
        }
        
        return res;
    }
    /*--------------------search in right---------------*/
       public static int numberOfColDiagonalRight(int dimensions, int r_q, int c_q, List<List<Integer>> arr){
        int startRow=r_q;
        int startCol=c_q+1;
        int res=0;
        while(startCol<=dimensions){
            if(searchInTwoDArray(arr, startRow,  startCol)){
                break;
            }
            res++;
            startCol++;
        }
        
        return res;
    }
    
    
    
}
 public static List<Integer> matchingStrings(List<String> stringList, List<String> queries) {
    // Write your code here
    List<Integer> response= new ArrayList<Integer>();
    for(int cmp=0; cmp<queries.size(); cmp++){
        int count=0;
        for(int cmp1=0; cmp1<stringList.size(); cmp1++){
            if(queries.get(cmp).equals(stringList.get(cmp1))){
                count++;
            }
        }
        response.add(count);
    }
    return response;

    }
"""