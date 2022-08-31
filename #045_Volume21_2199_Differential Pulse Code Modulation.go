//AOJ_Volume21_2199_Differential Pulse Code Modulation
//pythonは試していない（TLEしそうなので）
//goでmath使ってpowを計算したらTEL, 普通に2乗したら通った

package main
import "fmt"
import "bufio"
import "os"
//import "math"

const INF int = 1<<60

func main(){
    in := bufio.NewReader(os.Stdin)
    out := bufio.NewWriter(os.Stdout)
    defer out.Flush()

    for {
    	var N,M int
	    fmt.Fscan(in, &N,&M)
	    
	    if N == 0 && M == 0 {
	        break
	    } else {
	        
	        C := make([]int, M)
	        for k := 0; k < M; k++ {
	            var c int
	            fmt.Fscan(in, &c)
	            C[k] = c
            }
            
            X := make([]int, N)
	        for i := 0; i < N; i++ {
	            var x int
	            fmt.Fscan(in, &x)
	            X[i] = x
            }
//            fmt.Fprintln(out, C)
//            fmt.Fprintln(out, X)
            
            dp := make([][]int, N+3)
            for i := 0; i < N+3; i++ {
                dp[i] = make([]int, 256)
                for j := 0; j < 256; j++ {
                    dp[i][j] = INF
                }
            }
            dp[0][128] = 0
            
            for i := 0; i < N; i++ {
                x := X[i]
                for j := 0; j < 256; j++ {
                    if dp[i][j] == INF {
                        continue
                    } else {
                        for k := 0; k < M; k++ {
                            nxt := j + C[k]
                            if nxt < 0 {
                                nxt = 0
                            } else if nxt > 255 {
                                nxt = 255
                            }
//                            cal := int(math.Pow(float64(x - nxt), 2))
                            cal := (x-nxt)*(x-nxt)
                            if dp[i+1][nxt] > dp[i][j] + cal {
                                dp[i+1][nxt] = dp[i][j] + cal
                            }
                        }
                    }
                }
            }
            res := INF
            for j := 0; j < 256; j ++ {
                if dp[N][j] < res {
                    res = dp[N][j]
                }
            }
            fmt.Fprintln(out, res)
	    }
    }
}
