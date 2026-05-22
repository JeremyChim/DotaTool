import os.path

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QStringListModel, Qt
from ui import Ui_MainWindow
from script import *

heroes_path = os.path.join(path, "vpk", "pak01_dir", "scripts", "npc", "heroes")


class DotaToolWindow(QMainWindow, Ui_MainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_path = None
        self.cut_board = []
        self.undo_board = []
        self.init()

    def init(self):
        """初始化"""

        # 加载
        self.show_list()
        self._first_load()

        # 尺寸位置
        self.resize(1660, 880)
        self.move(160, 90)

        # 绑定
        self.listWidget.itemClicked.connect(self.open_file_form_list)
        self.lineEdit.textChanged.connect(self.show_list)

        # 快捷键
        self.action_tab.setShortcut("tab")

        # 文件
        self.action_load.triggered.connect(self.load)
        self.action_reload.triggered.connect(self.reload)
        self.action_save.triggered.connect(self.save)
        self.action_save_as.triggered.connect(self.save_as)
        self.action_open.triggered.connect(self.open)

        # 编辑
        self.action_cut.triggered.connect(self.cut)
        self.action_paste.triggered.connect(self.paste)
        self.action_undo.triggered.connect(self.undo)
        self.action_tab.triggered.connect(self.tab)
        self.action_back.triggered.connect(self.back)

        # 操作
        self.action_auto.triggered.connect(self.auto)
        self.action_oneline.triggered.connect(self.oneline)
        self.action_cd.triggered.connect(self.cd)
        self.action_sa.triggered.connect(self.sa)
        self.action_sp.triggered.connect(self.sp)
        self.action_ch.triggered.connect(self.ch)

        # 预设
        self.action_1.triggered.connect(lambda: self._fun("=1"))
        self.action_2.triggered.connect(lambda: self._fun("+2.5", "+5.0"))
        self.action_3.triggered.connect(lambda: self._fun("+25", "+50"))
        self.action_4.triggered.connect(lambda: self._fun("+250", "+500"))
        self.action_5.triggered.connect(lambda: self._fun("+50", "+100"))
        self.action_6.triggered.connect(lambda: self._fun("+500","+1000"))
        self.action_7.triggered.connect(lambda: self._fun("+50%"))
        self.action_8.triggered.connect(lambda: self._fun("+100%"))
        self.action_9.triggered.connect(lambda: self._fun("=999999"))
        self.action_0.triggered.connect(lambda: self._fun("=0"))
        self.action_add.triggered.connect(lambda: self._fun("+1"))
        self.action_ctrl_1.triggered.connect(lambda: self._fun("-1"))
        self.action_ctrl_2.triggered.connect(lambda: self._fun("-2.5", "-5.0"))
        self.action_ctrl_3.triggered.connect(lambda: self._fun("-25", "-50"))
        self.action_ctrl_4.triggered.connect(lambda: self._fun("-25%"))
        self.action_ctrl_5.triggered.connect(lambda: self._fun("-50%"))

        # 窗口
        self.action_top.triggered.connect(self.top)

        # 脚本
        self.action_vpk.triggered.connect(self.vpk)
        self.action_bot_cmd.triggered.connect(self.bot_cmd)
        self.action_steam_cmd.triggered.connect(self.steam_cmd)
        self.action_gi_open.triggered.connect(self.gi_open)
        self.action_gi.triggered.connect(self.gi)
        self.action_gi_reset.triggered.connect(self.gi_reset)
        self.action_clean_skin.triggered.connect(self.clean_skin)
        self.action_xp.triggered.connect(self.xp)
        self.action_item_time.triggered.connect(self.item_time)
        self.action_item.triggered.connect(self.item)
        self.action_path_dir.triggered.connect(self.path_dir)
        self.action_hero_dir.triggered.connect(self.hero_dir)
        self.action_bot_dir.triggered.connect(self.bot_dir)
        self.action_dota_dir.triggered.connect(self.dota_dir)
        self.action_mod_dir.triggered.connect(self.mod_dir)
        self.action_vscripts_dir.triggered.connect(self.vscripts_dir)
        self.action_skin_dir.triggered.connect(self.skin_dir)
        self.action_skin_dir2.triggered.connect(self.skin_dir2)
        self.action_skin_dir3.triggered.connect(self.skin_dir3)
        self.action_general_lua.triggered.connect(self.general_lua)
        self.action_killed_lua.triggered.connect(self.killed_lua)
        self.action_vpk_file.triggered.connect(self.vpk_file)
        self.action_config.triggered.connect(self.config)

    def show_list(self):
        text = self.lineEdit.text()
        dir_path = os.path.join(path, 'npc', 'heroes')
        heroes = os.listdir(dir_path)
        self.listWidget.clear()
        ls = []
        for hero in heroes:
            if text in hero:
                self.listWidget.addItem(hero)
                ls.append(hero)
        heroes_vpk = os.listdir(heroes_path)
        for i, hero in enumerate(ls):
            if hero in heroes_vpk:
                item = self.listWidget.item(i)
                item.setForeground(QColor('#FF00FF'))

    def open_file_form_list(self):
        file = self.listWidget.currentItem().text()
        file_path = os.path.join(heroes_path, file)
        if os.path.exists(file_path):
            lines = read_file(file_path)
            self.listView.setModel(QStringListModel(lines))
            self.file_path = file_path
            self.setWindowTitle(self.file_path)
            self.statusbar.showMessage(f"载入：{file_path}")
            return
        file_path = os.path.join(path, 'npc', 'heroes', file)
        if os.path.exists(file_path):
            lines = read_file(file_path)
            self.listView.setModel(QStringListModel(lines))
            self.file_path = file_path
            self.setWindowTitle(self.file_path)
            self.statusbar.showMessage(f"载入：{file_path}")
            return


    def load(self):
        """载入"""
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "npc/heroes")
        if file_path:
            file_path = os.path.abspath(file_path)
            lines = read_file(file_path)
            self.listView.setModel(QStringListModel(lines))
            self.file_path = file_path
            self.setWindowTitle(self.file_path)
            self.statusbar.showMessage(f"载入：{file_path}")

    def reload(self):
        """重载"""
        if self.file_path is not None:
            lines = read_file(self.file_path)
            self.listView.setModel(QStringListModel(lines))
            self.statusbar.showMessage(f"重载：{self.file_path}")
        else:
            self.statusbar.showMessage("没文件！")

    def save(self):
        """保存"""
        if self.file_path is not None:
            file_name = os.path.basename(self.file_path)
            save_path = os.path.join(heroes_path, file_name)
            write_file(save_path, self.listView.model().stringList())
            self.file_path = save_path
            self.setWindowTitle(self.file_path)
            self.show_list()
            self.statusbar.showMessage(f"保存：{save_path}")
        else:
            self.statusbar.showMessage("没文件！")

    def save_as(self):
        """另存"""
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", heroes_path)
        if file_path:
            file_path = os.path.abspath(file_path)
            write_file(file_path, self.listView.model().stringList())
            self.file_path = file_path
            self.setWindowTitle(self.file_path)
            self.show_list()
            self.statusbar.showMessage(f"另存为：{file_path}")

    def cut(self):
        """剪切"""
        line = self._read_line()
        if line:
            self.cut_board.append(self._tab_up(line))
            self._write_line("")
            self.statusbar.showMessage(f"剪切:{len(self.cut_board)}")

    def paste(self):
        """粘贴"""
        if len(self.cut_board) > 0:
            line = self._read_line()
            for lin in self.cut_board:
                line = line + lin
            self._write_line(line)
            self.cut_board = []
            self.statusbar.showMessage(f"粘贴!")

    def undo(self):
        """撤回"""
        if len(self.undo_board) > 0:
            self._write_line(self.undo_board[-1])
            self.undo_board = self.undo_board[:-1]
            self.statusbar.showMessage(f"撤回!")

    def tab(self):
        """缩进"""
        line = self._read_line()
        if line:
            line = self._tab_up(line)
            self._write_line(line)

    def back(self):
        """退格"""
        line = self._read_line()
        if line:
            line = self._tab_down(line)
            self._write_line(line)

    def open(self):
        """打开"""
        if os.path.exists(self.file_path):
            os.startfile(self.file_path)

    def auto(self):
        """自动"""
        try:
            sa = read_config()["sa"]
            sp = read_config()["sp"]
            sa_cd = read_config()["sa_cd"]
            sp_cd = read_config()["sp_cd"]
            line = self._read_line()

            if "value" in line or "special_bonus_unique" in line:
                line2 = self._update_ab1(line, sa, sp)
            elif "Point" in line or "Cooldown" in line or "ManaCost" in line or "RestoreTime" in line:
                line2 = self._update_ab2(line, sa_cd, sp_cd)
            else:
                line2 = self._update_ab2(line, sa, sp)
            self._write_line(line2)
            self.undo_board.append(line)
        except  Exception as e:
            self.statusbar.showMessage(str(e))

    def oneline(self):
        """单行"""
        sa = read_config()["sa"]
        sp = read_config()["sp"]
        line = self._read_line()
        line2 = self._update_ab1(line, sa, sp)
        self._write_line(line2)
        self.undo_board.append(line)

    def cd(self):
        """冷却"""
        sa_cd = read_config()["sa_cd"]
        sp_cd = read_config()["sp_cd"]
        line = self._read_line()
        if "value" in line:
            line2 = self._update_ab1(line, sa_cd, sp_cd)
        else:
            line2 = self._update_ab2(line, sa_cd, sp_cd)
        self._write_line(line2)
        self.undo_board.append(line)

    def sa(self):
        """魔晶"""
        try:
            sa = read_config()["sa"]
            sp = "n/a"
            line = self._read_line()
            line2 = self._update_ab1(line, sa, sp)
            self._write_line(line2)
            self.undo_board.append(line)
        except  Exception as e:
            self.statusbar.showMessage(str(e))

    def sp(self):
        """魔杖"""
        try:
            sa = "n/a"
            sp = read_config()["sp"]
            line = self._read_line()
            line2 = self._update_ab1(line, sa, sp)
            self._write_line(line2)
            self.undo_board.append(line)
        except  Exception as e:
            self.statusbar.showMessage(str(e))

    def ch(self):
        """充能"""
        try:
            line = self._read_line()
            line2 = self._ch(line)
            self._write_line(line2)
            self.undo_board.append(line)
        except  Exception as e:
            self.statusbar.showMessage(str(e))

    def top(self):
        """置顶"""
        if self.action_top.isChecked():
            self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
        self.show()

    def vpk(self):
        """生成vpk"""
        generate_vpk()
        self.statusbar.showMessage("生成vpk！")

    def bot_cmd(self):
        copy_bot_cmd()
        self.statusbar.showMessage("复制bot指令！")

    def steam_cmd(self):
        copy_steam_cmd()
        self.statusbar.showMessage("复制steam启动项！")

    def gi_open(self):
        open_gi()
        self.statusbar.showMessage("打开gameinfo.gi！")

    def gi(self):
        """更新gi"""
        update_gi()
        self.statusbar.showMessage("更新gi！")

    def gi_reset(self):
        """重置gi"""
        update_gi(reset=True)
        self.statusbar.showMessage("重置gi！")

    def clean_skin(self):
        clean_all_skin()
        self.statusbar.showMessage("清空皮肤！")

    def xp(self):
        """更新经验和金钱"""
        update_xp_gold()
        self.statusbar.showMessage("更新经验和金钱！")

    def item_time(self):
        """更新中立物品时间"""
        update_neutral_items()
        self.statusbar.showMessage("更新中立物品时间")

    def item(self):
        """更新物品"""
        update_items()
        self.statusbar.showMessage("更新物品！")

    def path_dir(self):
        """打开根目录"""
        open_path_dir()
        self.statusbar.showMessage("打开根目录！")

    def hero_dir(self):
        """打开英雄文件夹"""
        open_hero_dir()
        self.statusbar.showMessage("打开英雄文件夹！")

    def bot_dir(self):
        """打开bot文件夹"""
        open_bot_dir()
        self.statusbar.showMessage("打开bot文件夹！")

    def dota_dir(self):
        """打开dota文件夹"""
        open_dota_path()
        self.statusbar.showMessage("打开dota文件夹！")

    def mod_dir(self):
        """打开mod文件夹"""
        open_mod_dir()
        self.statusbar.showMessage("打开mod文件夹！")

    def vscripts_dir(self):
        """打开vscripts文件夹"""
        open_vscripts_dir()
        self.statusbar.showMessage("打开vscripts文件夹！")

    def skin_dir(self):
        """打开 Dota2SkinChanger 文件夹"""
        open_skin_dir()
        self.statusbar.showMessage("打开 Dota2SkinChanger 文件夹！")

    def skin_dir2(self):
        """打开 Dota2SkinChanger2 文件夹"""
        open_skin_dir2()
        self.statusbar.showMessage("打开 Dota2SkinChanger2 文件夹！")

    def skin_dir3(self):
        """打开 Dota2SkinChanger3 文件夹"""
        open_skin_dir3()
        self.statusbar.showMessage("打开 Dota2SkinChanger2 文件夹！")

    def general_lua(self):
        """打开general.lua文件"""
        open_general_lua()
        self.statusbar.showMessage("打开general.lua文件！")

    def killed_lua(self):
        """打开OnEntityKilled.lua"""
        open_on_entity_killed_lua()
        self.statusbar.showMessage("打开OnEntityKilled.lua文件！")

    def vpk_file(self):
        """打开pak01_dir.vpk"""
        open_vpk()
        self.statusbar.showMessage("打开vpk文件！")

    def config(self):
        """打开config.json"""
        open_config()
        self.statusbar.showMessage("打开config.json文件！")

    # region 工具方法

    def closeEvent(self, event):
        """关闭事件"""
        config = read_config()
        config["last_path"] = self.file_path
        write_config(config)

    def _first_load(self):
        last_path = read_config()["last_path"]
        if last_path is None: return
        if os.path.exists(last_path):
            file_path = os.path.abspath(last_path)
            lines = read_file(file_path)
            self.listView.setModel(QStringListModel(lines))
            self.file_path = file_path
            self.setWindowTitle(self.file_path)
            self.statusbar.showMessage(f"载入：{file_path}")
        else:
            self.file_path = None

    def _read_line(self):
        index = self.listView.selectionModel().currentIndex()
        return index.data()

    def _write_line(self, line):
        index = self.listView.selectionModel().currentIndex()
        self.listView.model().setData(index, line)

    def _update_ab1(self, line, sa, sp):
        val_line = f'[tab]"[ab_name]"\t\t"[ab_val]"\n'
        sa_line = f'[tab]"special_bonus_shard"\t\t"{sa}"\n'
        sp_line = f'[tab]"special_bonus_scepter"\t\t"{sp}"\n'

        if sa == "n/a":
            mod = val_line + sp_line
        elif sp == "n/a":
            mod = val_line + sa_line
        else:
            mod = val_line + sa_line + sp_line

        cut = line.split('"')
        return mod.replace("[tab]", cut[0]).replace("[ab_name]", cut[1]).replace("[ab_val]", cut[3])

    def _update_ab2(self, line, sa, sp):
        name_line = f'[tab]"[ab_name]"\n'
        start_line = '[tab]{\n'
        val_line = f'[tab]\t"value"\t\t"[ab_val]"\n'
        sa_line = f'[tab]\t"special_bonus_shard"\t\t"{sa}"\n'
        sp_line = f'[tab]\t"special_bonus_scepter"\t\t"{sp}"\n'
        end = '[tab]}\n'

        if sa == "n/a":
            mod = name_line + start_line + val_line + sp_line + end
        elif sp == "n/a":
            mod = name_line + start_line + val_line + sa_line + end
        else:
            mod = name_line + start_line + val_line + sa_line + sp_line + end

        cut = line.split('"')
        return mod.replace("[tab]", cut[0]).replace("[ab_name]", cut[1]).replace("[ab_val]", cut[3])

    def _tab_up(self, line):
        ls = line.split('\n')
        ls2 = []
        for l in ls:
            l = '\t' + l
            ls2.append(l)
        return '\n'.join(ls2)

    def _tab_down(self, line):
        ls = line.split('\n')
        ls2 = []
        for l in ls:
            if len(l) != 0 and l[0] == '\t':
                ls2.append(l[1:])
            else:
                ls2.append(l)
        return '\n'.join(ls2)

    def _fun(self, a, b=None):
        try:
            if b is None: b = a
            line = self._read_line()
            if "value" in line or "special_bonus_unique" in line:
                line2 = self._update_ab1(line, a, b)
            else:
                line2 = self._update_ab2(line, a, b)
            self._write_line(line2)
            self.undo_board.append(line)
        except  Exception as e:
            self.statusbar.showMessage(str(e))

    def _ch(self, line):
        mod = '''
"AbilityCharges"		
{
    "value"						"1"
    "special_bonus_shard"		"+1"
    "special_bonus_scepter"		"+1"
}
"AbilityChargeRestoreTime"
{
    "value"		"21 18 15 12"
    "special_bonus_shard"		"-25%"
    "special_bonus_scepter"		"-50%"
    "special_bonus_unique_morphling_waveform_cooldown"			"-40%"
}
"AbilityCooldown"		
{
    "value"		"0"
    "special_bonus_shard"		"-25%"
    "special_bonus_scepter"		"-50%"
    "special_bonus_unique_morphling_waveform_cooldown"			"-40%"
}
'''
        return line + mod
    # endregion


if __name__ == '__main__':
    app = QApplication([])
    win = DotaToolWindow()
    win.show()
    app.exec_()
