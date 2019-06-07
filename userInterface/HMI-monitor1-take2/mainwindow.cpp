#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QMediaPlayer>
#include <QNetworkRequest>
#include <QVideoWidget>
#include <QLabel>
#include <QApplication>
#include <QDesktopWidget>
#include <QVBoxLayout>
#include <QTimer>
#include <QWindow>
#include <QTime>
#include <QFont>
#include <QtMultimedia>
#include <QProcess>
#include <QFile>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    mRunning(false),
    mStartTime(),
    mLabel(new QLabel("0:0:0:0"))
{
    ui->setupUi(this);
    formatTimer();

    // set window title
    setWindowTitle("Monitor 1: Microscope");
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    // create video widget
    QVideoWidget *video = new QVideoWidget;
    // create media player
    QMediaPlayer *player = new QMediaPlayer;

    //add video widget
    mainLayout->addWidget(video);
    // add timer under video display
    QHBoxLayout *timerDisplay = new QHBoxLayout;
    timerDisplay->addWidget(mLabel);
    mainLayout->addLayout(timerDisplay);
    //add buttons
    QHBoxLayout *buttonsLayout = new QHBoxLayout;
    QPushButton *startButton = new QPushButton("Start StopWatch");
    connect(startButton, SIGNAL(clicked()), SLOT(start()));
    buttonsLayout->addWidget(startButton);
    stopButton = new QPushButton("Stop StopWatch");
    connect(stopButton, SIGNAL(clicked()), SLOT(stop()));
    buttonsLayout->addWidget(stopButton);
    QPushButton *flagbutton = new QPushButton("Flag");
    connect(flagbutton, SIGNAL(clicked()), SLOT(flag()));
    buttonsLayout->addWidget(flagbutton);
    buttonsLayout->addStretch();
    mainLayout->addLayout(buttonsLayout);

    //create main widget to hold layout
    QWidget *win = new QWidget();
    win->setLayout(mainLayout);
    setCentralWidget(win);
    player->setVideoOutput(video);
    // link RTSP to Videos
    const QUrl url1 = QUrl("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"); //change IP address to correct camera
    // network request the URLs
    const QNetworkRequest requestRtsp1(url1);
    // set the request to player
    player->setMedia(requestRtsp1);
    // start streaming
    player->play();

    startTimer(0);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::start(void)
{
    stopButton->setText("Recording in progress");
    QString command = "ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -i :0.0 -t 00:00:30 /home/anette/tester3.mp4";
    proc.start("/bin/bash", QStringList() << "-c" << command);
    proc.waitForStarted();

    mStartTime = QDateTime::currentDateTime();
    mRunning = true;
}

void MainWindow::stop(void)
{
    proc.close();
    mRunning = false;
}

void MainWindow::timerEvent(QTimerEvent *)
{

    if(mRunning)
    {
        qint64 ms = mStartTime.msecsTo(QDateTime::currentDateTime());
        long int h = ms / 1000 / 60 / 60;
        long int m = (ms / 1000 / 60) - (h * 60);
        long int s = (ms / 1000) - (m * 60);
        ms = ms - (s * 1000);
        QString diff = QString("%1:%2:%3:%4").arg(h).arg(m).arg(s).arg(ms);
        mLabel->setText(diff);

        if(mLabel->text() == "0:0:30:0") {
            stopButton->setText("Recording stopped");
        }
    }
}

void MainWindow::formatTimer(void) {
    QFont font = mLabel->font();
    font.setPointSize(32);
    font.setBold(true);
    mLabel->setFont(font);
}

void MainWindow::flag(void) {
    file1.setFileName(filename);
    QByteArray ba = mLabel->text().toLocal8Bit();
    const char* add = ba.data();
    if ( file1.open(QIODevice::WriteOnly | QIODevice::Append) )
    {
        file1.write(add);
        file1.write("\n");
    }
    file1.close();
}
