//ALDS1_ALDS1_10_C_Longest_Common_Subsequence
//ナップザックDP, PythonでTLE, 同様の解き方にてgoでAC

package main
import "fmt"
import "bufio"
import "os"

func main(){
    in := bufio.NewReader(os.Stdin)
    out := bufio.NewWriter(os.Stdout)
    defer out.Flush()
    
    var N int
    fmt.Fscan(in,&N)
    
    for i := 0; i < N; i++ {
        var lx,ly int
        var X,Y string
        fmt.Fscan(in,&X)
        fmt.Fscan(in,&Y)
        lx = len(X)
        ly = len(Y)
        
        dp := make([][]int, ly+1)
        for j := 0; j < ly+1; j++ {
            dp[j] = make([]int, lx+1)
        }
        
        for h := 0; h < ly; h++ {
            for w := 0; w < lx; w++ {
                if dp[h][w+1] > dp[h+1][w+1] {
                    dp[h+1][w+1] = dp[h][w+1]
                }
                if X[w] == Y[h] {
                    if dp[h][w]+1 > dp[h+1][w+1] {
                        dp[h+1][w+1] = dp[h][w] + 1
                    }
                } else {
                    if dp[h+1][w] > dp[h+1][w+1] {
                        dp[h+1][w+1] = dp[h+1][w]
                    } else if dp[h][w+1] > dp[h+1][w+1] {
                        dp[h+1][w+1] = dp[h][w+1]
                    }
                }
            }
        }

//    for j := 0; j < ly+1; j++ {
//        fmt.Fprintln(out,dp[j])
    res := 0
    for i := 0; i < lx+1; i++ {
        if dp[ly][i] > res {
            res = dp[ly][i]
        }
    }
    fmt.Fprintln(out,res)
    }
}    
    
    
