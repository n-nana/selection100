//DPL_DPL_2_A_Traveling_Salesman_Problem
//bit-DP(巡回セールスマン問題)
//Python TLE

package main
import "fmt"
import "bufio"
import "os"
import "math"

const INF int = 1<<60
var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main(){
    defer out.Flush()

	var V,E int
	fmt.Fscan(in, &V,&E)
  
    //隣接グラフ
    G := make([][]int, V)
    for i := 0; i < V; i++ {
        G[i] = make([]int, V)
        for j := 0; j < V; j++ {
            G[i][j] = -1
        }
    }
    
    for i := 0; i < E; i++ {
        var s,t,d int
        fmt.Fscan(in, &s,&t,&d)
        G[s][t] = d
    }
    
    mx := int(math.Pow(2,float64(V)))
    dp := make([][]int, mx)
    for i := 0; i < mx; i++ {
        dp[i] = make([]int, V)
        for j := 0; j < V; j++ {
            dp[i][j] = INF
        }
    }
    dp[0][0] = 0
    
    // 左bitシフト 1<<jでコンパイルエラー(AOJ環境)
    // jを符号なしint: uintにしたら通った
    for k := 0; k < mx-1; k++ {
        for i := 0; i < V; i++ {
            for j := 0; j < V; j++ {
                if G[i][j] == -1 {
                    continue
                }
                if k&(1<<uint(j)) != 0 {
                    continue
                }
                if dp[k][i] + G[i][j] < dp[k|(1<<uint(j))][j] {
                    dp[k|(1<<uint(j))][j] = dp[k][i] + G[i][j]
                }
            }
        }
    }
    ans := dp[mx-1][0]
    if ans == INF {
        fmt.Fprintln(out, -1)
    } else {
        fmt.Fprintln(out, ans)
    }
    
//    fmt.Fprintln(out, dp)
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
