#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QDateTime>
#include <QProcess>
#include <QFile>

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
    void start(void);
    void stop(void);
    void flag(void);

private:
    Ui::MainWindow *ui;
    bool mRunning;
    QDateTime mStartTime;
    QLabel *mLabel;
    QProcess proc;
    QPushButton *stopButton;
    QPushButton *timeflag;
    QString filename="/home/anette/flags.txt";
    QFile file1;
};

#endif // MAINWINDOW_H

