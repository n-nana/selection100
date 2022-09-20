
//Daruma Otoshi
//https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=ja
//区間DP
//Python TLE....
//https://kakedashi-engineer.appspot.com/2020/06/17/aoj1611/

package main
import "fmt"
import "bufio"
import "os"

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main(){
    defer out.Flush()
    for {
    	var N int
	    fmt.Fscan(in, &N)
        if N == 0 {
            break
        }
        
        W := make([]int, N)
        for i := 0; i < N; i++ {
            var w int
            fmt.Fscan(in, &w)
            W[i] = w
        }
        //fmt.Fprintln(out, W)
        
        dp := make([][]int, N+3) //DPテーブル
        for i := 0; i < N+3; i++ {
            dp[i] = make([]int, N+3)
        }
        
        for length := 1; length < N; length++ { //みている範囲の大きさ
            for i := 0; i < N-length; i++ { //始点index
                j := i + length //終点index
                
                if (length+1)%2 == 1 { //次にみる範囲の大きさが奇数（追加で消せない）
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                } else { //次にみる範囲の大きさが偶数
                    if dp[i+1][j-1] == length-1 { //両端以外を全て消せる場合
                        dp[i][j] = dp[i+1][j-1]
                        if abs(W[j]- W[i]) <= 1 { //さらに両端を消せる場合
                            dp[i][j] += 2
                        }
                    }
                    for k := i+1; k < j; k++ {
                        dp[i][j] = max(dp[i][k] + dp[k+1][j], dp[i][j])
                    }
                }
                
            }
        }
        ans := dp[0][N-1]
        fmt.Fprintln(out, ans)
//        for i := 0; i < N; i++ {
//            fmt.Fprintln(out, dp[i])
//        }
//        fmt.Fprintln(out)
        
    }
}


//-------------------------------------------------------------
func max(a,b int) int {
    if a < b {
        return b
    } else {
        return a
    }
}

func min(a,b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}

func abs(a int) int {
    if a < 0 {
        return -a
    } else {
        return a
    }
}
