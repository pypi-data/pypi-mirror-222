def p1():
    return """#include <stdio.h>

int main()
{
    int i, j, k = 0;
    int flag = 1, a[16], g[16], r[20], div[16], n, m;

    printf("\nEnter the degree of generator: ");
    scanf("%d", &n);

    printf("Enter the generator: ");
    for (i = 0; i <= n; i++)
        scanf("%d", &g[i]);

    printf("Enter the degree of frames: ");
    scanf("%d", &m);

    printf("Enter the frame: ");
    for (i = 0; i <= m; i++)
        scanf("%d", &a[i]);

    if (m < n || (g[0] && g[n]) == 0)
    {
        printf("Not a proper generator\n");
    }

    for (i = m + 1; i <= m + n; i++)
        a[i] = 0;

    for (j = 0; j <= n; j++)
        r[j] = a[j];

    for (i = n; i <= m + n; i++)
    {
        if (i > n)
        {
            for (j = 0; j < n; j++)
                r[j] = r[j + 1];
            r[j] = a[i];
        }

        if (r[0])
            div[k++] = 1;
        else
        {
            div[k++] = 0;
            continue;
        }

        for (j = 0; j <= n; j++)
            r[j] = r[j] ^ g[j];
    }

    printf("\nQuotient is: ");
    for (j = 0; j < k; j++)
        printf("%d ", div[j]);

    printf("\nRemainder is: ");
    for (i = 1; i <= n; i++)
        printf("%d", r[i]);

    printf("\nTransmitted frame is: ");
    for (i = m + 1, j = 1; i <= m + n; i++, j++)
        a[i] = r[j];

    for (i = 0; i <= m + n; i++)
        printf("%d", a[i]);

    printf("\n");

    printf("\nEnter the degree of frame: ");
    scanf("%d", &m);

    printf("\nEnter the frame: ");
    for (i = 0; i <= m; i++)
        scanf("%d", &a[i]);

    for (j = 0; j <= n; j++)
        r[j] = a[j];

    k = 0;

    for (i = n; i <= m; i++)
    {
        if (i > n)
        {
            for (j = 0; j < n; j++)
                r[j] = r[j + 1];
            r[j] = a[i];
        }

        if (r[0])
            div[k++] = 1;
        else
        {
            div[k++] = 0;
            continue;
        }

        for (j = 0; j <= n; j++)
            r[j] = r[j] ^ g[j];
    }

    printf("\nQuotient is: ");
    for (j = 0; j < k; j++)
        printf("%d", div[j]);

    printf("\nRemainder is: ");
    for (i = 1; i <= n; i++)
        printf("%d", r[i]);

    for (i = 1; i <= n; i++)
    {
        if (r[i])
            flag = 0;
    }

    if (flag)
        printf("\nNo error\n");
    else
        printf("\nError\n");
}
"""

def p2():
    return """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct frame
{
    int seq;
    int len;
    int flag;
    char data[10];
} n[20], m[20], temp;

char str[100];
int count = 0;

void frames()
{
    int i, j, s, size, total = 0;
    s = strlen(str);

    while (total < s)
    {
        size = rand() % 10 + 1;
        n[count].seq = count + 1;
        n[count].len = size;
        n[count].flag = 0;

        if ((total + size) < s)
        {
            for (i = total, j = 0; j < size; i++, j++)
                n[count].data[j] = str[i];
            total += size;
        }
        else
        {
            n[count].len = s - total;
            for (j = 0; j < n[count].len; j++)
                n[count].data[j] = str[total++];
        }
        count += 1;
    }

    printf("\nShow the packets:\n\n");
    for (i = 0; i < count; i++)
    {
        printf("\t%d:%d\t", n[i].seq, n[i].len);
        for (j = 0; j < n[i].len; j++)
            printf("%c", n[i].data[j]);
        printf("\n");
    }
}

void trans()
{
    int i, j;
    int c = 0;

    while (c < count)
    {
        i = rand() % count;
        if (n[i].flag == 0)
        {
            m[c++] = n[i];
            n[i].flag = 1;
        }
    }

    printf("\n\nShow the random packets:\n\n");
    for (i = 0; i < count; i++)
    {
        printf("\t%d:%d\t", m[i].seq, m[i].len);
        for (j = 0; j < m[i].len; j++)
            printf("%c", m[i].data[j]);
        printf("\n");
    }
}

void sort()
{
    int i, j;

    for (i = 0; i < count; i++)
        for (j = i + 1; j < count; j++)
            if (m[i].seq > m[j].seq)
            {
                temp = m[i];
                m[i] = m[j];
                m[j] = temp;
            }

    printf("\n\nShow the sequenced packets:\n\n");
    for (i = 0; i < count; i++)
    {
        printf("\t%d:%d\t", m[i].seq, m[i].len);
        for (j = 0; j < m[i].len; j++)
            printf("%c", m[i].data[j]);
        printf("\n");
    }
}

int main()
{
    system("clear");
    printf("Enter the data: ");
    scanf("%s", str);
    frames();
    trans();
    sort();

    return 0;
}
"""

def p3():
    return """#include <stdio.h>

struct node
{
    unsigned dist[20];
    unsigned from[20];
} rt[10];

int main()
{
    int costmat[20][20];
    int nodes, i, j, k, count = 0;

    printf("\nEnter the number of nodes: ");
    scanf("%d", &nodes);

    printf("\nEnter the cost matrix:\n");
    for (i = 0; i < nodes; i++)
    {
        for (j = 0; j < nodes; j++)
        {
            scanf("%d", &costmat[i][j]);
            costmat[i][i] = 0;
            rt[i].dist[j] = costmat[i][j]; // initialize the distance equal to the cost matrix
            rt[i].from[j] = j;
        }
    }

    do
    {
        count = 0;
        for (i = 0; i < nodes; i++)
        {
            // We choose an arbitrary vertex k and we calculate the direct distance from node i to k using the cost matrix
            // and add the distance from k to node j
            for (j = 0; j < nodes; j++)
            {
                for (k = 0; k < nodes; k++)
                {
                    if (rt[i].dist[j] > costmat[i][k] + rt[k].dist[j])
                    {
                        // We calculate the minimum distance
                        rt[i].dist[j] = rt[i].dist[k] + rt[k].dist[j];
                        rt[i].from[j] = k;
                        count++;
                    }
                }
            }
        }
    } while (count != 0);

    for (i = 0; i < nodes; i++)
    {
        printf("\n\nFor router %d\n", i + 1);
        for (j = 0; j < nodes; j++)
        {
            printf("\t\nnode %d via %d Distance %d ", j + 1, rt[i].from[j] + 1, rt[i].dist[j]);
        }
    }

    printf("\n\n");
    return 0;
}
"""

def p4():
    return """#include <stdio.h>
#include <string.h>

int main()
{
    int count, src_router, i, j, k, w, v, min;
    int cost_matrix[100][100], dist[100], last[100];
    int flag[100];

    printf("\nEnter the number of routers: ");
    scanf("%d", &count);

    printf("\nEnter the cost matrix values:\n");
    for (i = 0; i < count; i++)
    {
        for (j = 0; j < count; j++)
        {
            printf("%d->%d: ", i, j);
            scanf("%d", &cost_matrix[i][j]);
            if (cost_matrix[i][j] < 0)
                cost_matrix[i][j] = 1000;
        }
    }

    printf("\nEnter the source router: ");
    scanf("%d", &src_router);

    for (v = 0; v < count; v++)
    {
        flag[v] = 0;
        last[v] = src_router;
        dist[v] = cost_matrix[src_router][v];
    }

    flag[src_router] = 1;

    for (i = 0; i < count; i++)
    {
        min = 1000;
        for (w = 0; w < count; w++)
        {
            if (!flag[w] && dist[w] < min)
            {
                v = w;
                min = dist[w];
            }
        }

        flag[v] = 1;

        for (w = 0; w < count; w++)
        {
            if (!flag[w] && min + cost_matrix[v][w] < dist[w])
            {
                dist[w] = min + cost_matrix[v][w];
                last[w] = v;
            }
        }
    }

    for (i = 0; i < count; i++)
    {
        printf("\n%d ==> %d: Path taken: %d", src_router, i, i);
        w = i;
        while (w != src_router)
        {
            printf("\n<--%d", last[w]);
            w = last[w];
        }
        printf("\nShortest path cost: %d", dist[i]);
    }

    printf("\n");

    return 0;
}
"""

def p5():
    return """#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>

int t_rand(int a)
{
    int rn;
    rn = random() % 10;
    rn = rn % a;
    if (rn == 0)
        rn = 1;
    return (rn);
}

int main()
{
    int i, j, clk, packets[5], o_rate, i_rate, b_size, p_remain, p_sz, p_sz_rm = 0, p_time, flag = 0;

    system("clear");

    printf("Enter 5 packets in the stream:\n");
    for (i = 0; i < 5; ++i)
    {
        scanf("%d", &packets[i]);
    }

    printf("\nEnter the Output Rate: ");
    scanf("%d", &o_rate);

    printf("\nEnter the Bucket Size: ");
    scanf("%d", &b_size);

    for (i = 0; i < 5; ++i)
    {
        if ((packets[i] + p_sz_rm) > b_size)
        {
            if (packets[i] > b_size)
                printf("\n\nIncoming packet size (%d) is GREATER than bucket capacity - !!!REJECTED!!!", packets[i]);
            else
                printf("\nBucket capacity exceeded - !!!REJECTED!!!");
        }
        else
        {
            for (j = 0;; ++j)
            {
                p_remain = 4 - i;
                p_sz = packets[i];
                p_sz_rm += p_sz;
                printf("\n\nIncoming Packet Size: %d", p_sz);
                printf("\nTransmission Left: %d", p_sz_rm);
                p_time = t_rand(5) * 2;
                printf("\n\nNext Packet will come at: %d", p_time);
                for (clk = 0; clk < p_time; clk += 1)
                {
                    printf("\nTime left: %d", clk);
                    sleep(1);
                    if (p_sz_rm)
                    {
                        printf(" - !!!Transmitted!!!");
                        if (p_sz_rm <= o_rate)
                            p_sz_rm = 0;
                        else
                            p_sz_rm -= o_rate;
                        printf(" - Bytes Remaining: %d", p_sz_rm);
                    }
                    else
                    {
                        printf(" - No Packets to transmit!!!");
                    }
                }

                if (p_sz_rm != 0)
                    flag = 1;
                break;
            }
        }
    }

    printf("\n\n");
    return (0);
}
"""

def p6():
    return """#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define FIFO1_NAME "Server_fifo"
#define FIFO2_NAME "Client_fifo"

int main()
{
    char p[100], c[300];
    int num, num2, f1, fd, fd2;

    mknod(FIFO1_NAME, S_IFIFO | 0666, 0);
    mknod(FIFO2_NAME, S_IFIFO | 0666, 0);

    printf("\nServer is online!!!...\n");
    fd = open(FIFO1_NAME, O_RDONLY);
    printf("\nClient is online!\n");

    while (1)
    {
        if ((num = read(fd, p, 100)) == -1)
            perror("read error");
        else
        {
            p[num] = '\0';
            if ((f1 = open(p, O_RDONLY)) < 0)
            {
                printf("\nServer %s is not found", p);
                exit(1);
            }
            else
            {
                printf("Server %s found!\nTransferring the content\n", p);
                stdin = fdopen(f1, "r");
                while (!feof(stdin))
                {
                    if (fgets(c, 300, stdin) != NULL)
                    {
                        fd2 = open(FIFO2_NAME, O_WRONLY);
                        if ((num2 = write(fd2, c, strlen(c))) == -1)
                            perror("Transfer error");
                    }
                    else
                        perror("read");
                }
                printf("Server transfer completed\n");
                exit(1);
            }
        }
    }
    return 1;
}
//client//
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define FIFO1_NAME "Server_fifo"
#define FIFO2_NAME "Client_fifo"

int main()
{
    char p[100], c[300];
    int num, num2, fd, fd2;

    mknod(FIFO1_NAME, S_IFIFO | 0666, 0);
    mknod(FIFO2_NAME, S_IFIFO | 0666, 0);

    printf("\nWaiting for server...\n");
    fd = open(FIFO1_NAME, O_WRONLY);
    printf("\nServer online!\nClient: Enter the path\n");

    while (gets(p), !feof(stdin))
    {
        if ((num = write(fd, p, strlen(p))) == -1)
            perror("write error");
        else
        {
            printf("\nWaiting for reply....\n");
            fd2 = open(FIFO2_NAME, O_RDONLY);
            if ((num2 = read(fd2, c, 300)) == -1)
                perror("transfer error!\n");
            else
            {
                printf("File received! Displaying the contents:\n");
                if (fputs(c, stdout) == EOF)
                    perror("print error");
                exit(1);
            }
        }
    }
    return 0;
}
"""

def p7():
    return """#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include <signal.h>

#define MYPORT 6490
#define BACKLOG 10

int main(void)
{
    int sockfd, fp, new_fd;
    struct sockaddr_in my_addr, their_addr;
    int sin_size, i = 0;
    int yes = 1;
    char buf1[20], buf2[20000];

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("socket");
        exit(1);
    }

    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1)
    {
        perror("setsockopt");
        exit(1);
    }

    my_addr.sin_family = AF_INET;
    my_addr.sin_port = htons(MYPORT);
    my_addr.sin_addr.s_addr = INADDR_ANY;
    memset(&(my_addr.sin_zero), '\0', 8);

    if (bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr)) == -1)
    {
        perror("bind");
        exit(1);
    }

    if (listen(sockfd, BACKLOG) == -1)
    {
        perror("listen");
        exit(1);
    }

    printf("\nServer is online!!!!\nServer waiting for the client\n");
    sin_size = sizeof(struct sockaddr_in);
    if ((new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &sin_size)) == -1)
    {
        perror("accept");
        exit(0);
    }

    printf("\nServer got connection from %s\n", inet_ntoa(their_addr.sin_addr));
    recv(new_fd, &buf1, sizeof(buf1), 0);
    printf("File request is %s\n", buf1);

    if ((fp = open(buf1, O_RDONLY)) < 0)
    {
        printf("File not found\n");
        strcpy(buf2, "file not found");
    }
    else
    {
        printf("SERVER: %s found and ready to transfer\n", buf1);
        read(fp, &buf2, 20000);
        close(fp);
    }

    send(new_fd, &buf2, sizeof(buf2), 0);
    close(new_fd);
    close(sockfd);
    printf("\nTransfer successful\n");
    printf("\n");

    return 0;
}
//client//
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <fcntl.h>
#include <netdb.h>
#include <errno.h>

#define PORT 6490

int main()
{
    int sockfd;
    char buf1[40], buf2[20000];
    struct sockaddr_in their_addr;

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("socket");
        exit(1);
    }

    their_addr.sin_family = AF_INET;
    their_addr.sin_port = htons(PORT);
    their_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    memset(&(their_addr.sin_zero), '\0', 8);

    if (connect(sockfd, (struct sockaddr *)&their_addr, sizeof(struct sockaddr)) == -1)
    {
        perror("connect");
        exit(1);
    }

    printf("Client is online\n");
    printf("\nClient: Enter the filename to be displayed: ");
    scanf("%s", buf1);
    send(sockfd, buf1, sizeof(buf1), 0);

    if (recv(sockfd, buf2, sizeof(buf2), 0) == 1)
    {
        perror("recv");
        exit(1);
    }
    else
    {
        printf("\nDisplaying the contents of %s\n", buf1);
        printf("%s\n", buf2);
    }

    close(sockfd);
    return 0;
}
"""

def p8():
    return """ #include <stdio.h>
#include <math.h>

double min(double x, double y)
{
    return (x < y ? x : y);
}

double max(double x, double y)
{
    return (x > y ? x : y);
}

double gcd(double x, double y)
{
    if (x == y)
        return x;
    else
        return gcd(min(x, y), max(x, y) - min(x, y));
}

long double modexp(long double a, long double x, long double n)
{
    long double r = 1;
    while (x > 0)
    {
        if ((int)(fmodl(x, 2)) == 1)
        {
            r = fmodl((r * a), n);
        }
        a = fmodl((a * a), n);
        x /= 2;
    }
    return r;
}

int main()
{
    long double p, q, phi, n, e, d, ms, es, ds;
    system("clear");

    do
    {
        printf("\nEnter prime numbers P and Q: ");
        scanf("%Lf %Lf", &p, &q);
    } while (p == q);

    n = p * q;
    phi = (p - 1) * (q - 1);

    do
    {
        printf("\nEnter prime value of e: ");
        scanf("%Lf", &e);
    } while ((gcd(e, phi) != 1) && e > phi);

    for (d = 1; d < phi; ++d)
    {
        if (fmod((e * d), phi) == 1)
            break;
    }

    printf("\nD within main = %Lf", d);

    printf("\nEnter the message: ");
    scanf("%Lf", &ms);

    es = modexp(ms, e, n);
    ds = modexp(es, d, n);

    printf("\nOriginal message: %Lf", ms);
    printf("\nEncrypted message: %Lf", es);
    printf("\nDecrypted message: %Lf\n\n", ds);

    return 0;
}
"""