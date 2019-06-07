#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QDateTime>
#include <QtMultimedia>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void formatTimer(void);

protected:
    void timerEvent(QTimerEvent *);


private slots:
    void saveScreenshot(); //keep this function
    //void shootScreen(); //maybe won't need anymore
    void startTimer1(void);
    void startTimer2(void);
    void startTimer3(void);
    void startTimer4(void);
    void startTimer5(void);

    void flash1(void);
    void flash2(void);
    void flash3(void);
    void flash4(void);
    void flash5(void);

    //new functions
    void shootCam1(void);
    void shootCam3(void);

    //void delay();

private:
    Ui::MainWindow *ui;
    QPixmap originalPixmap;

    bool run1;
    bool run2;
    bool run3;
    bool run4;
    bool run5;

    QDateTime st1;
    QDateTime st2;
    QDateTime st3;
    QDateTime st4;
    QDateTime st5;

    QLabel *clock1;
    QLabel *clock2;
    QLabel *clock3;
    QLabel *clock4;
    QLabel *clock5;

    QVideoWidget *video1;
    QVideoWidget *video2;
    QVideoWidget *video3;
    QVideoWidget *video4;
    QWidget *win;
    QVBoxLayout *mainLayout;
    QGridLayout *layout;
    QString camName;
    QString expName = "";

    QVBoxLayout *tbox1;
    QVBoxLayout *tbox2;
    QVBoxLayout *tbox3;
    QVBoxLayout *tbox4;
    QVBoxLayout *tbox5;

    QPushButton *tbutton1;
    QPushButton *tbutton2;
    QPushButton *tbutton3;
    QPushButton *tbutton4;
    QPushButton *tbutton5;

    QTime ct;
};

#endif // MAINWINDOW_H
