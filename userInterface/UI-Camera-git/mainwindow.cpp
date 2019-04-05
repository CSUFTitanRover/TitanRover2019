#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QCoreApplication>
#include <QDebug>
#include <QGridLayout>
#include <QMediaPlayer>
#include <QNetworkRequest>
#include <QVideoWidget>
#include <QComboBox>
#include <QLabel>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Name Window
    setWindowTitle("Camera Views");

    // Create camera widget
    cameraWidget = new QVideoWidget;
    cameraWidget1 = new QVideoWidget;
    cameraWidget2 = new QVideoWidget;
    cameraWidget3 = new QVideoWidget;
    cameraWidget4 = new QVideoWidget;


    // Create media player(for sound)
    _player = new QMediaPlayer;
    _player1 = new QMediaPlayer;
    _player2 = new QMediaPlayer;
    _player3 = new QMediaPlayer;
    _player4 = new QMediaPlayer;


    //make buttons
    pbc1 = new QPushButton("GO");
    pbc2 = new QPushButton("GO");
    pbc3 = new QPushButton("GO");
    pbc4 = new QPushButton("GO");


    //make camera labels
    QLabel *l1 = new QLabel;
    QLabel *l2 = new QLabel;
    QLabel *l3 = new QLabel;
    QLabel *l4 = new QLabel;
    l1->setText("Camera 1");
    l1->setAlignment(Qt::AlignCenter);
    l1->setFixedHeight(20);
    l2->setText("Camera 2");
    l2->setAlignment(Qt::AlignCenter);
    l2->setFixedHeight(20);
    l3->setText("Camera 3");
    l3->setFixedHeight(20);
    l3->setAlignment(Qt::AlignCenter);
    l4->setText("Camera 4");
    l4->setFixedHeight(20);
    l4->setAlignment(Qt::AlignCenter);

    //make dropdown buttons
    cb1 = new QComboBox;
    cb2 = new QComboBox;
    cb3 = new QComboBox;
    cb4 = new QComboBox;
    cb1->addItem("No Stream");
    cb1->addItem("High Res", "http://192.168.1.2:8081/");
    cb1->addItem("Medium Res", "http://192.168.1.2:8081/");
    cb1->addItem("Low Res", "http://192.168.1.2:8081/");
    cb2->addItem("No Stream", "http://192.168.1.2:8081/");
    cb2->addItem("High Res", "http://192.168.1.2:8081/");
    cb2->addItem("Medium Res", "http://192.168.1.2:8081/");
    cb2->addItem("Low Res", "http://192.168.1.2:8081/");
    cb3->addItem("No Stream", "http://192.168.1.2:8081/");
    cb3->addItem("High Res", "http://192.168.1.2:8081/");
    cb3->addItem("Medium Res", "http://192.168.1.2:8081/");
    cb3->addItem("Low Res", "http://192.168.1.2:8081/");
    cb4->addItem("No Stream", "http://192.168.1.2:8081/");
    cb4->addItem("High Res", "http://192.168.1.2:8081/");
    cb4->addItem("Medium Res", "http://192.168.1.2:8081/");
    cb4->addItem("Low Res", "http://192.168.1.2:8081/");



    //Create QGridLayout 4x6
    layout = new QGridLayout;
    layout->addWidget(l1,0,0,1,4);
    layout->addWidget(l2,0,4,1,4);
    layout->addWidget(l3,0,8,1,4);
    layout->addWidget(l4,0,12,1,4);
    layout->addWidget(cb1,1,0,1,3);
    layout->addWidget(cb2,1,4,1,3);
    layout->addWidget(cb3,1,8,1,3);
    layout->addWidget(cb4,1,12,1,3);
    layout->addWidget(pbc1,1,3,1,1);
    layout->addWidget(pbc2,1,7,1,1);
    layout->addWidget(pbc3,1,11,1,1);
    layout->addWidget(pbc4,1,15,1,1);
    layout->addWidget(cameraWidget,2,0,3,16);


    // Create a QWidget to hold video widget
    QWidget *win = new QWidget();
    win->setLayout(layout);
    setCentralWidget(win);

    // QMediaPlayer -> QVideoWidget
    _player1->setVideoOutput(cameraWidget1);
    _player2->setVideoOutput(cameraWidget2);
    _player3->setVideoOutput(cameraWidget3);
    _player4->setVideoOutput(cameraWidget4);


    //connect button functions
    connect(pbc1, SIGNAL (clicked()), this, SLOT (setCamera1()));
    connect(pbc2, SIGNAL (clicked()), this, SLOT (setCamera2()));
    connect(pbc3, SIGNAL (clicked()), this, SLOT (setCamera3()));
    connect(pbc4, SIGNAL (clicked()), this, SLOT (setCamera4()));




    // Links RTSP to Video
    //for testing:      rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov
    //for testing:      rtsp://b1.dnsdojo.com:1935/live/sys3.stream
    QNetworkRequest requestRtspc1(QUrl("http://192.168.1.2:8081"));
    QNetworkRequest requestRtspc2(QUrl("http://192.168.1.2:8082"));
    QNetworkRequest requestRtspc3(QUrl("http://192.168.1.2:8083"));
    QNetworkRequest requestRtspc4(QUrl("http://192.168.1.2:8084"));

    //connect network to video stream
    _player1->setMedia(requestRtspc1);
    _player2->setMedia(requestRtspc2);
    _player3->setMedia(requestRtspc3);
    _player4->setMedia(requestRtspc4);

    //play streams
    _player1->play();
    _player2->play();
    _player3->play();
    _player4->play();

    loadqual.load(QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=0"));
    loadqual.load(QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=0"));
    loadqual.load(QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=0"));
    loadqual.load(QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=0"));






}

//function to set camera 1
void MainWindow::setCamera1() {
    int ind = cb1->currentIndex();
    QUrl qurl;

    if(ind == 1) {
        //stream high res
        qurl = QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=30");
    }
    else if(ind == 2) {
        //stream medium res
        qurl = QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=15");
    }
    else if(ind == 3) {
        //stream low res
        qurl = QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=5");
    }
    else {
        //no stream
        qurl = QUrl("");
    }

    //change stream quality
    loadqual.load(qurl);

    if(cameraPlay != 1) {
        layout->removeItem(layout->itemAtPosition(2,0));
        delete layout->itemAtPosition(2,0);


        if(cameraPlay == 2) {
            cameraWidget2->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=0");
        }
        else if(cameraPlay == 3) {
            cameraWidget3->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=0");
        }
        else if(cameraPlay == 4) {
            cameraWidget4->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=0");
        }
        loadqual.load(q);


        layout->addWidget(cameraWidget1,2,0,3,16); //last digit was 16
        cameraWidget1->setVisible(true);
        //_player1->play();
    }

    //set other cameras to "no stream"
    cb2->setCurrentText("No Stream");
    cb3->setCurrentText("No Stream");
    cb4->setCurrentText("No Stream");

    cameraPlay = 1;
}

//function to set camera 2
void MainWindow::setCamera2() {
    int ind = cb2->currentIndex();
    QUrl qurl;

    if(ind == 1) {
        //stream high res
        qurl = QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=30");
    }
    else if(ind == 2) {
        //stream medium res
        qurl = QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=15");
    }
    else if(ind == 3) {
        //stream low res
        qurl = QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=5");
    }
    else {
        //no stream
        qurl = QUrl("");
    }

    loadqual.load(qurl);

    if(cameraPlay != 2) {
        layout->removeItem(layout->itemAtPosition(2,0));
        delete layout->itemAtPosition(2,0);

        //layout->removeWidget(layout->itemAtPosition(2, 0)->widget()); //delete if not functional
        if(cameraPlay == 1) {
            cameraWidget1->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=0");
        }
        else if(cameraPlay == 3) {
            cameraWidget3->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=0");
        }
        else if(cameraPlay == 4) {
            cameraWidget4->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=0");
        }
        loadqual.load(q);


        layout->addWidget(cameraWidget2,2,0,3,16);
        cameraWidget2->setVisible(true);
        //_player2->play();
    }


    //set other cameras to "no stream"
    cb1->setCurrentText("No Stream");
    cb3->setCurrentText("No Stream");
    cb4->setCurrentText("No Stream");

    cameraPlay = 2;
}

//function to set camera 3
void MainWindow::setCamera3() {
    int ind = cb3->currentIndex();
    QUrl qurl;

    if(ind == 1) {
        //stream high res
        qurl = QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=30");
    }
    else if(ind == 2) {
        //stream medium res
        qurl = QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=15");
    }
    else if(ind == 3) {
        //stream low res
        qurl = QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=5");
    }
    else {
        //no stream
        qurl = QUrl("");
    }

    loadqual.load(qurl);

    if(cameraPlay != 3) {
        layout->removeItem(layout->itemAtPosition(2,0));
        delete layout->itemAtPosition(2,0);

        if(cameraPlay == 1) {
            cameraWidget1->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=0");
        }
        else if(cameraPlay == 2) {
            cameraWidget2->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=0");
        }
        else if(cameraPlay == 4) {
            cameraWidget4->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=0");
        }
        loadqual.load(q);

        layout->addWidget(cameraWidget3,2,0,3,16);
        cameraWidget3->setVisible(true);
        //_player3->play();
    }

    //set other cameras to "no stream"
    cb1->setCurrentText("No Stream");
    cb2->setCurrentText("No Stream");
    cb4->setCurrentText("No Stream");

    cameraPlay = 3;
}

//function to set camera 4
void MainWindow::setCamera4() {
    int ind = cb4->currentIndex();
    QUrl qurl;

    if(ind == 1) {
        //stream high res
        qurl = QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=30");
    }
    else if(ind == 2) {
        //stream medium res
        qurl = QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=15");
    }
    else if(ind == 3) {
        //stream low res
        qurl = QUrl("http://192.168.1.2:8080/4/config/set?stream_quality=5");
    }
    else {
        //no stream
        qurl = QUrl("");
    }

    loadqual.load(qurl);

    if(cameraPlay != 4) {
        layout->removeItem(layout->itemAtPosition(2,0));
        delete layout->itemAtPosition(2,0);

        if(cameraPlay == 1) {
            cameraWidget1->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/1/config/set?stream_quality=0");
        }
        else if(cameraPlay == 3) {
            cameraWidget3->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/3/config/set?stream_quality=0");
        }
        else if(cameraPlay == 2) {
            cameraWidget2->setVisible(false);
            q = QUrl("http://192.168.1.2:8080/2/config/set?stream_quality=0");
        }
        loadqual.load(q);
        layout->addWidget(cameraWidget4,2,0,3,16);
        cameraWidget4->setVisible(true);
        //_player4->play();
    }

    //set other cameras to "no stream"
    cb1->setCurrentText("No Stream");
    cb2->setCurrentText("No Stream");
    cb3->setCurrentText("No Stream");

    cameraPlay = 4;
}

MainWindow::~MainWindow()
{
    delete ui;
}
