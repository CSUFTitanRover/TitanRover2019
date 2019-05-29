#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QGridLayout>
#include <QMediaPlayer>
#include <QNetworkRequest>
#include <QVideoWidget>
#include <QLabel>
#include <QApplication>
#include <QDesktopWidget>
#include <QPixmap>
#include <QVBoxLayout>
#include <QTimer>
#include <QDir>
#include <QImageWriter>
#include <QWindow>
#include <QScreen>
#include <QTime>
#include <QFont>
#include <QtMultimedia>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    run1(false),
    run2(false),
    run3(false),
    run4(false),
    run5(false),
    clock1(new QLabel("0:0:0:0")),
    clock2(new QLabel("0:0:0:0")),
    clock3(new QLabel("0:0:0:0")),
    clock4(new QLabel("0:0:0:0")),
    clock5(new QLabel("0:0:0:0"))
{
    ui->setupUi(this);
    formatTimer();

    // set window title
    setWindowTitle("Monitor 2: HMI Camera Views");
    mainLayout = new QVBoxLayout(this);
    // create video widget
    video1 = new QVideoWidget;
    video2 = new QVideoWidget;
    video3 = new QVideoWidget;
    video4 = new QVideoWidget;
    // create media player
    QMediaPlayer *player1 = new QMediaPlayer;
    QMediaPlayer *player2 = new QMediaPlayer;
    QMediaPlayer *player3 = new QMediaPlayer;
    QMediaPlayer *player4 = new QMediaPlayer;

    //add video widgets
    layout = new QGridLayout;
    layout->addWidget(video1,0,0,1,1);
    layout->addWidget(video2,0,1,1,1);
    layout->addWidget(video3,1,0,1,1);
    layout->addWidget(video4,1,1,1,1);
    mainLayout->addLayout(layout);

    //timers
    QHBoxLayout *timerDisplay = new QHBoxLayout;

    tbox1 = new QVBoxLayout;
    tbox1->addWidget(new QLabel("Experiment 1"));
    tbox1->addWidget(clock1);
    tbutton1 = new QPushButton("Start Timer");
    connect(tbutton1, SIGNAL(clicked()), SLOT(startTimer1()));
    tbox1->addWidget(tbutton1);
    timerDisplay->addLayout(tbox1);

    tbox2 = new QVBoxLayout;
    tbox2->addWidget(new QLabel("Experiment 2"));
    tbox2->addWidget(clock2);
    tbutton2 = new QPushButton("Start Timer");
    connect(tbutton2, SIGNAL(clicked()), SLOT(startTimer2()));
    tbox2->addWidget(tbutton2);
    timerDisplay->addLayout(tbox2);

    tbox3 = new QVBoxLayout;
    tbox3->addWidget(new QLabel("Experiment 3"));
    tbox3->addWidget(clock3);
    tbutton3 = new QPushButton("Start Timer");
    connect(tbutton3, SIGNAL(clicked()), SLOT(startTimer3()));
    tbox3->addWidget(tbutton3);
    timerDisplay->addLayout(tbox3);

    tbox4 = new QVBoxLayout;
    tbox4->addWidget(new QLabel("Experiment 4"));
    tbox4->addWidget(clock4);
    tbutton4 = new QPushButton("Start Timer");
    connect(tbutton4, SIGNAL(clicked()), SLOT(startTimer4()));
    tbox4->addWidget(tbutton4);
    timerDisplay->addLayout(tbox4);

    tbox5 = new QVBoxLayout;
    tbox5->addWidget(new QLabel("Experiment 5"));
    tbox5->addWidget(clock5);
    tbutton5 = new QPushButton("Start Timer");
    connect(tbutton5, SIGNAL(clicked()), SLOT(startTimer5()));
    tbox5->addWidget(tbutton5);
    timerDisplay->addLayout(tbox5);

    // add timer under video display
    mainLayout->addLayout(timerDisplay);



    //add buttons
    QHBoxLayout *buttonsLayout = new QHBoxLayout;
    QPushButton *screen1 = new QPushButton("Screenshot Camera 1");
    connect(screen1, SIGNAL(clicked()), SLOT(shootCam1()));
    buttonsLayout->addWidget(screen1);
    QPushButton *screen3 = new QPushButton("Screenshot Camera 3");
    connect(screen3, SIGNAL(clicked()), SLOT(shootCam3()));
    buttonsLayout->addWidget(screen3);
    QPushButton *quitScreenshotButton = new QPushButton(tr("Quit"), this);
    quitScreenshotButton->setShortcut(Qt::CTRL + Qt::Key_Q);
    connect(quitScreenshotButton, &QPushButton::clicked, this, &QWidget::close);
    buttonsLayout->addWidget(quitScreenshotButton);
    buttonsLayout->addStretch();
    mainLayout->addLayout(buttonsLayout);

    //create main widget to hold quads
    win = new QWidget();
    win->setLayout(mainLayout);
    setCentralWidget(win);

    player1->setVideoOutput(video1);
    player2->setVideoOutput(video2);
    player3->setVideoOutput(video3);
    player4->setVideoOutput(video4);

    // link RTSP to Videos
    const QUrl url1 = QUrl("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"); //change IP address to correct camera
    const QUrl url2 = QUrl("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"); //change IP address to correct camera
    const QUrl url3 = QUrl("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"); //change IP address to correct camera
    const QUrl url4 = QUrl("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"); //change IP address to correct camera

    // network request the URLs
    const QNetworkRequest requestRtsp1(url1);
    const QNetworkRequest requestRtsp2(url2);
    const QNetworkRequest requestRtsp3(url3);
    const QNetworkRequest requestRtsp4(url4);

    // set the request to player
    player1->setMedia(requestRtsp1);
    player2->setMedia(requestRtsp2);
    player3->setMedia(requestRtsp3);
    player4->setMedia(requestRtsp4);

    // start streaming
    player1->play();
    player2->play();
    player3->play();
    player4->play();

    startTimer(0);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::saveScreenshot()
{
    //may not need ct anymore
    const QString format = "png";
    QString initialPath = "/home/anette/savedScreenShots";
    ct = QTime::currentTime();
    initialPath += "/" + camName + expName + ct.toString() + "." + format;

    QStringList mimeTypes;
    foreach (const QByteArray &bf, QImageWriter::supportedMimeTypes())
        mimeTypes.append(QLatin1String(bf));

    QFile file(initialPath);
    file.open(QIODevice::WriteOnly);
    originalPixmap.save(&file, "PNG");
}

void MainWindow::shootCam1(void) {
    QScreen *scr = QGuiApplication::primaryScreen();
    if (const QWindow *window = windowHandle())
        scr = window->screen();
    if (!scr)
        return;

    originalPixmap = scr->grabWindow(video1->winId());
    camName = "Camera1-";
    saveScreenshot();
}

void MainWindow::shootCam3(void) {
    QScreen *scr = QGuiApplication::primaryScreen();
    if (const QWindow *window = windowHandle())
        scr = window->screen();
    if (!scr)
        return;

    originalPixmap = scr->grabWindow(video3->winId());
    camName = "Camera3-";
    saveScreenshot();
}

void MainWindow::startTimer1(void) {
    st1 = QDateTime::currentDateTime();
    run1 = true;
}

void MainWindow::startTimer2(void) {
    st2 = QDateTime::currentDateTime();
    run2 = true;
}

void MainWindow::startTimer3(void) {
    st3 = QDateTime::currentDateTime();
    run3 = true;
}

void MainWindow::startTimer4(void) {
    st4 = QDateTime::currentDateTime();
    run4 = true;
}

void MainWindow::startTimer5(void) {
    st5 = QDateTime::currentDateTime();
    run5 = true;
}

void MainWindow::timerEvent(QTimerEvent *)
{
    //screenshot camera 3

    if(run1) {
        qint64 ms = st1.msecsTo(QDateTime::currentDateTime());
        long int h = ms / 1000 / 60 / 60;
        long int m = (ms / 1000 / 60) - (h * 60);
        long int s = (ms / 1000) - (m * 60);
        ms = ms - (s * 1000);
        QString diff = QString("%1:%2:%3:%4").arg(h).arg(m).arg(s).arg(ms);
        clock1->setText(diff);

        //0:0:30:0
        if(diff == "0:0:10:0") {
            expName = "Sample_1_at_30sec_";
            shootCam3();
            //expName = "";
            qDebug("run 1 @ 30");
        }

        //0:4:30:0
        if(diff == "0:0:20:0") {
            flash1();
            qDebug("run 1 start flash");
        }

        //0:5:0:0
        if(diff == "0:0:30:0") {
            expName = "Sample_1_at_5min_";
            shootCam3();
            //expName = "";
            run1 = false;
            flash1();
            qDebug("run 1 @ 5");
        }

    }

    if(run2) {
        qint64 ms = st2.msecsTo(QDateTime::currentDateTime());
        long int h = ms / 1000 / 60 / 60;
        long int m = (ms / 1000 / 60) - (h * 60);
        long int s = (ms / 1000) - (m * 60);
        ms = ms - (s * 1000);
        QString diff = QString("%1:%2:%3:%4").arg(h).arg(m).arg(s).arg(ms);
        clock2->setText(diff);

        //0:0:30:0
        if(diff == "0:0:10:0") {
            expName = "Sample_2_at_30sec_";
            shootCam3();
            expName = "";
            qDebug("run 2 @ 30");
        }

        //0:4:30:0
        if(diff == "0:0:20:0") {
            flash2();
            qDebug("run 2 start flash");
        }

        //0:5:0:0
        if(diff == "0:0:30:0") {
            expName = "Sample_2_at_5min_";
            shootCam3();
            expName = "";
            run2 = false;
            flash2();
            qDebug("run 2 @ 5");
        }
    }

    if(run3) {
        qint64 ms = st3.msecsTo(QDateTime::currentDateTime());
        long int h = ms / 1000 / 60 / 60;
        long int m = (ms / 1000 / 60) - (h * 60);
        long int s = (ms / 1000) - (m * 60);
        ms = ms - (s * 1000);
        QString diff = QString("%1:%2:%3:%4").arg(h).arg(m).arg(s).arg(ms);
        clock3->setText(diff);

        //0:0:30:0
        if(diff == "0:0:10:0") {
            expName = "Sample_3_at_30sec_";
            shootCam3();
            expName = "";
            qDebug("run 3 @ 30");
        }

        //0:4:30:0
        if(diff == "0:0:20:0") {
            flash3();
            qDebug("run 3 start flash");
        }

        //0:5:0:0
        if(diff == "0:0:30:0") {
            expName = "Sample_3_at_5min_";
            shootCam3();
            expName = "";
            run3 = false;
            flash3();
            qDebug("run 3 @ 5");
        }
    }

    if(run4) {
        qint64 ms = st4.msecsTo(QDateTime::currentDateTime());
        long int h = ms / 1000 / 60 / 60;
        long int m = (ms / 1000 / 60) - (h * 60);
        long int s = (ms / 1000) - (m * 60);
        ms = ms - (s * 1000);
        QString diff = QString("%1:%2:%3:%4").arg(h).arg(m).arg(s).arg(ms);
        clock4->setText(diff);

        //0:0:30:0
        if(diff == "0:0:10:0") {
            expName = "Sample_4_at_30sec_";
            shootCam3();
            expName = "";
            qDebug("run 4 @ 30");
        }

        //0:4:30:0
        if(diff == "0:0:20:0") {
            flash4();
            qDebug("run 4 start flash");
        }

        //0:5:0:0
        if(diff == "0:0:30:0") {
            expName = "Sample_4_at_5min_";
            shootCam3();
            expName = "";
            run4 = false;
            flash4();
            qDebug("run 4 @ 5");
        }
    }

    if(run5) {
        qint64 ms = st5.msecsTo(QDateTime::currentDateTime());
        long int h = ms / 1000 / 60 / 60;
        long int m = (ms / 1000 / 60) - (h * 60);
        long int s = (ms / 1000) - (m * 60);
        ms = ms - (s * 1000);
        QString diff = QString("%1:%2:%3:%4").arg(h).arg(m).arg(s).arg(ms);
        clock5->setText(diff);

        //0:0:30:0
        if(diff == "0:0:10:0") {
            expName = "Sample_5_at_30sec_";
            shootCam3();
            expName = "";
            qDebug("run 5 @ 30");
        }

        //0:4:30:0
        if(diff == "0:0:20:0") {
            flash5();
            qDebug("run 5 start flash");
        }

        //0:5:0:0
        if(diff == "0:0:30:0") {
            expName = "Sample_5_at_5min_";
            shootCam3();
            expName = "";
            run5 = false;
            flash5();
            qDebug("run 5 @ 5");
        }
    }
}

void MainWindow::formatTimer(void) {
    QFont font;
    font.setPointSize(16);
    clock1->setFont(font);
    clock2->setFont(font);
    clock3->setFont(font);
    clock4->setFont(font);
    clock5->setFont(font);

}

void MainWindow::flash1(void) {
    QPalette pal = tbutton1->palette();

    if(run1) {
        pal.setColor(QPalette::Button, QColor(Qt::red));
        tbutton1->setAutoFillBackground(true);
        tbutton1->setFlat(true);
        tbutton1->setPalette(pal);
        tbutton1->update();
    }
    else {
        tbutton1->setAutoFillBackground(false);
        tbutton1->setFlat(false);
        tbutton1->update();
    }
}

void MainWindow::flash2(void) {
    QPalette pal = tbutton2->palette();

    if(run2) {
        pal.setColor(QPalette::Button, QColor(Qt::red));
        tbutton2->setAutoFillBackground(true);
        tbutton2->setFlat(true);
        tbutton2->setPalette(pal);
        tbutton2->update();
    }
    else {
        tbutton2->setAutoFillBackground(false);
        tbutton2->setFlat(false);
        tbutton2->update();
    }
}

void MainWindow::flash3(void) {
    QPalette pal = tbutton3->palette();

    if(run3) {
        pal.setColor(QPalette::Button, QColor(Qt::red));
        tbutton3->setAutoFillBackground(true);
        tbutton3->setFlat(true);
        tbutton3->setPalette(pal);
        tbutton3->update();
    }
    else {
        tbutton3->setAutoFillBackground(false);
        tbutton3->setFlat(false);
        tbutton3->update();
    }
}

void MainWindow::flash4(void) {
    QPalette pal = tbutton4->palette();

    if(run4) {
        pal.setColor(QPalette::Button, QColor(Qt::red));
        tbutton4->setAutoFillBackground(true);
        tbutton4->setFlat(true);
        tbutton4->setPalette(pal);
        tbutton4->update();
    }
    else {
        tbutton4->setAutoFillBackground(false);
        tbutton4->setFlat(false);
        tbutton4->update();
    }
}

void MainWindow::flash5(void) {
    QPalette pal = tbutton5->palette();

    if(run5) {
        pal.setColor(QPalette::Button, QColor(Qt::red));
        tbutton5->setAutoFillBackground(true);
        tbutton5->setFlat(true);
        tbutton5->setPalette(pal);
        tbutton5->update();
    }
    else {
        tbutton5->setAutoFillBackground(false);
        tbutton5->setFlat(false);
        tbutton5->update();
    }
}
