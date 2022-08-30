//AOJ_Volume11_1166_Pollock's conjecture
//2次元->1次元DP, PythonでTLE, 同様の解き方にてgoでAC

package main
import "fmt"
import "bufio"
import "os"

const INF int = 1<<60
const mx int = 1000000

func main(){
    in := bufio.NewReader(os.Stdin)
    out := bufio.NewWriter(os.Stdout)
    defer out.Flush()

    dp1 := make([]int, mx+5)
    dp2 := make([]int, mx+5)
    for i := 0; i < mx+5; i++ {
        dp1[i] = INF
        dp2[i] = INF
    dp1[0] = 0
    dp2[0] = 0
    }
    
    for i := 0; i < 200; i++ {
        p := (i+1)*(i+2)*(i+3)/6
        for j := 0; j < mx+1; j++ {
            if p <= j {
                if dp1[j-p] + 1 < dp1[j] {
                    dp1[j] = dp1[j-p] + 1
                }
                if p%2 == 1 {
                    if dp2[j-p] + 1 < dp2[j] {
                        dp2[j] = dp2[j-p] + 1
                    }
                }
            }
        }
    }
    
    for {
        var N int
	    fmt.Fscan(in, &N)
        if N == 0 {
            break
        } else {
            fmt.Fprintln(out, dp1[N],dp2[N])
        }
    }
}
