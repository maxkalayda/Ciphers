import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import QtQuick.Controls.Material 2.0

ApplicationWindow {
    id: window
    visible: true
    width: 1024
    height: 768
    title: qsTr("CryptoApp")

    Material.theme: Material.Light
    Material.primary: Material.Blue
    Material.accent: Material.Blue
    header: ToolBar{
        ToolButton {
            id: toolButton
            text: stackView.depth > 1 ? "\u25C0" : "\u2630"
            font.pixelSize: Qt.application.font.pixelSize * 1.6
            onClicked: {
                if (stackView.depth > 1) {
                    stackView.pop()
                } else {
                    drawer.open()
                }
            }
        }

        Label{
            text: stackView.currentItem.title
            anchors.centerIn: parent
            color: "white"
        }
    }
    Drawer{
        id: drawer
        width: window.width * 0.24
        height: window.height
        background: Rectangle{
            Rectangle{
                color: Material.color(Material.Grey)
                width: drawer.width
                height: drawer.height
            }
        }
            Column{
                id: columnDrawer
                spacing: 5
                padding: 5
                Button {
                    id: buttonCaesar
                    text: qsTr("Шифр Цезаря")
                    width: drawer.width - 10
                    Material.background: Material.Blue
                    Material.elevation: 3
                    contentItem: Text{
                        color: "white"
                        text: buttonCaesar.text
                        font: buttonCaesar.font
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                    onClicked:{
                        stackView.push("Caesar.ui.qml")
                        drawer.close()
                    }
                }
                Button {
                    id: buttonAtbash
                    text: qsTr("Шифр Атбаш")
                    width: drawer.width - 10
                    Material.background: Material.Blue
                    Material.elevation: 3
                    contentItem: Text{
                        color: "white"
                        text: buttonAtbash.text
                        font: buttonAtbash.font
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                    onClicked:{
                        stackView.push("Caesar.ui.qml")
                        drawer.close()
                    }
                }
    } // end colum
}    

    StackView{
        id: stackView
        initialItem: "Home.ui.qml"
        anchors.fill: parent
    }
}
