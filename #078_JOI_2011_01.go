//2次元累積和
//pythonではTLE

package main
import "fmt"
import "bufio"
import "os"

//import "reflect"
//import "sort"
//import "strconv"
//import "strings"

const MOD1 int = 998244353
var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main(){
    defer out.Flush()

	var H,W,K int
	fmt.Fscan(in, &H,&W,&K)
    
    //辞書型
    dct := map[string]int{
        "J": 0,
        "O": 1,
        "I": 2,
    }
    
    G := make([]string, H)
    for i := 0; i < H; i++ {
        var g string
        fmt.Fscan(in, &g)
        G[i] = g
    }

    // 3次元
    P := make([][][]int, 3)
    for i := 0; i < 3; i++ {
        P[i] = make([][]int, H+1)
        for j := 0; j < H+1; j++ {
            P[i][j] = make([]int, W+1)
            for k := 0; k < W+1; k++ {
                P[i][j][k] = 0
            }
        }
    }
    
    for j := 0; j < H; j++ {
        cnt := make([]int, 3)
        for k := 0; k < W; k++ {
            idx := dct[string(G[j][k])]
            cnt[idx] ++
            for i := 0; i < 3; i++ {
                P[i][j+1][k+1] = P[i][j][k+1] + cnt[i]
            }
        }
    }
    
    for q := 0; q < K; q++ {
        var a,b,c,d int
	    fmt.Fscan(in, &a,&b,&c,&d)
	    res := make([]int, 3)
	    for i := 0; i < 3; i++ {
	        res[i] = P[i][c][d] - P[i][c][b-1] - P[i][a-1][d] + P[i][a-1][b-1]
	    }
	    
	    fmt.Fprintln(out, res[0], res[1], res[2])
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

