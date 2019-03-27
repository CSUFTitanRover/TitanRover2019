#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMediaPlayer>
#include <QNetworkRequest>
#include <QVideoWidget>
#include <QComboBox>
#include <QLabel>
#include <QPushButton>
#include <QWebView>
#include <QGridLayout>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void setCamera1();
    void setCamera2();
    void setCamera3();
    void setCamera4();

private:
    Ui::MainWindow *ui;
    QGridLayout *layout;
    QVideoWidget *cameraWidget1;
    QVideoWidget *cameraWidget2;
    QVideoWidget *cameraWidget3;
    QVideoWidget *cameraWidget4;
    QVideoWidget *cameraWidget;
    QMediaPlayer *_player;
    QMediaPlayer *_player1;
    QMediaPlayer *_player2;
    QMediaPlayer *_player3;
    QMediaPlayer *_player4;
    QPushButton *pbc1;
    QPushButton *pbc2;
    QPushButton *pbc3;
    QPushButton *pbc4;
    QComboBox *cb1;
    QComboBox *cb2;
    QComboBox *cb3;
    QComboBox *cb4;
    QUrl c1url = QUrl("http://192.168.1.2:8081/");
    QUrl c2url = QUrl("http://192.168.1.2:8082/");
    QUrl c3url = QUrl("http://192.168.1.2:8083/");
    QUrl c4url = QUrl("http://192.168.1.2:8084/");
    QUrl q;
    QWebView loadqual;
    int cameraPlay = 0;
};

#endif // MAINWINDOW_H
