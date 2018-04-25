import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import QtQuick.Controls.Material 2.0

Page{
    id: pageWin
    anchors.fill: parent
    Rectangle{
        id: mainRect
        width: parent.width
        height: parent.height/2
        anchors.centerIn: parent.Center
        color: "red"
        GridLayout{
            rows: 3
            columns: 3
            width: parent.width
                Rectangle{
                    Layout.row: 0
                    Layout.column: 0
                    Layout.columnSpan: 2
                    Layout.preferredHeight: 200
                    Layout.preferredWidth: 600
                    color: "blue"
                        TextArea{
                            id: txtSource
                            placeholderText: qsTr("Введите текст")
                            wrapMode: "Wrap"
                            focus: true
                            //Layout.row: 0
                            //Layout.column: 0
                            //Layout.columnSpan: 2
                            font.pointSize: 10
                            anchors.centerIn: parent.Center
                            //Layout.preferredHeight: 200
                            //Layout.preferredWidth: 600
                            background: Rectangle{
                                anchors.fill: parent
                                border.color: "#2196F3"
                            }
                       }
                }
        }
     }
}

//            TextArea{
//                id: txtSource
//                placeholderText: qsTr("Введите текст")
//                wrapMode: "Wrap"
//                focus: true
//                width: 600
//                font.pointSize: 10
//                background: Rectangle{
//                    implicitHeight: 200
//                    implicitWidth: 650
//                    border.color: "#2196F3"
//                }
//           }
//            Button {
//                id: button
//                anchors.left: txtSource.right
//                text: qsTr("Зашифровать")
//                width: drawer.width
//                Material.background: Material.Blue
//                Material.elevation: 3
//                contentItem: Text{
//                    color: "white"
//                    text: button.text
//                    font: button.font
//                    horizontalAlignment: Text.AlignHCenter
//                    verticalAlignment: Text.AlignVCenter
//                }
//            }

