import subprocess
import shutil
import pyperclip
import json
import os

path = os.getcwd()
bat_path = os.path.join(path, "vpk", "vpk.bat")
gi_path = os.path.join(path, "gi", "gameinfo_branchspecific.gi")
gi_path2 = os.path.join(path, "gi", "gameinfo_branchspecific2.gi")
units_path = os.path.join(path, "npc", "npc_units.txt")
units_path2 = os.path.join(path, "vpk", "pak01_dir", "scripts", "npc", "npc_units.txt")
neutral_items_path = os.path.join(path, "npc", "neutral_items.txt")
neutral_items_path2 = os.path.join(path, "vpk", "pak01_dir", "scripts", "npc", "neutral_items.txt")
items_path = os.path.join(path, "npc", "items.txt")
items_path2 = os.path.join(path, "vpk", "pak01_dir", "scripts", "npc", "items.txt")


def read_config():
    """读配置"""
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def write_config(config):
    """写配置"""
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)


def read_file(file_path):
    """读文件"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def write_file(file_path, lines):
    """写文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def generate_vpk():
    """生成vpk"""
    config = read_config()
    mod_path = os.path.join(config["dota_path"], "game", "mod")
    subprocess.run(bat_path, shell=True)
    vpk_path = os.path.join(path, "vpk", "pak01_dir.vpk")
    vpk_path2 = os.path.join(mod_path, "pak01_dir.vpk")
    print(vpk_path, vpk_path2)
    os.makedirs(mod_path, exist_ok=True)
    shutil.move(vpk_path, vpk_path2)


def copy_bot_cmd():
    """复制bot指令"""
    config = read_config()
    bot_cmd = config["bot_cmd"]
    pyperclip.copy(bot_cmd)
    print(bot_cmd)


def copy_steam_cmd():
    """复制steam指令"""
    config = read_config()
    steam_cmd = config["steam_cmd"]
    pyperclip.copy(steam_cmd)
    print(steam_cmd)


def update_xp_gold():
    """更新xp和金币"""
    config = read_config()
    xp = config["xp"]
    gold = config["gold"]
    lines2 = []
    lines = read_file(units_path)
    for i, line in enumerate(lines):
        if "BountyXP" in line:
            val = line.split('"')[3]
            res = eval(val + xp)
            line2 = line.replace(val, str(int(res)))
            print(i + 1, line, end='')
            print(i + 1, line2, end='')
            lines2.append(line2)
        elif "BountyGoldMin" in line or "BountyGoldMax" in line:
            val = line.split('"')[3]
            res = eval(val + gold)
            line2 = line.replace(val, str(int(res)))
            print(i + 1, line, end='')
            print(i + 1, line2, end='')
            lines2.append(line2)
        else:
            lines2.append(line)
    write_file(units_path2, lines2)


def update_neutral_items():
    """更新中立物品时间"""
    config = read_config()
    times = config["times"]
    lines2 = []
    lines = read_file(neutral_items_path)
    x = 0
    for i, line in enumerate(lines):
        if "start_time" in line:
            t = line.split('"')[3]
            t2 = times[x]
            line2 = line.replace(t, t2)
            lines2.append(line2)
            x += 1
            print(i + 1, line2, end='')
        elif "madstone_no_limit_time" in line:
            t = line.split('"')[3]
            t2 = times[-1]
            line2 = line.replace(t, t2)
            lines2.append(line2)
            print(i + 1, line2, end='')
        else:
            lines2.append(line)
    write_file(neutral_items_path2, lines2)


def update_items():
    config = read_config()
    infos = config["infos"]
    lines = read_file(items_path)
    lines2 = lines[:]
    for info in infos:
        name, attr, new_val = info
        line2 = 'n/a \n'
        i = 0
        for i, line in enumerate(lines):
            if f'"{name}"' in line:
                print(i + 1, line, end='')
                break
        for i, line in enumerate(lines[i:], i):
            if f'"{attr}"' in line:
                val = line.split('"')[3]
                line2 = line.replace(val, new_val)
                print(i + 1, line2, end='')
                break
        lines2[i] = line2
    write_file(items_path2, lines2)


def update_gi(reset=False):
    dota_path = read_config()['dota_path']
    gi_path3 = os.path.join(dota_path, "game", "dota", "gameinfo_branchspecific.gi")
    if reset:
        lines3 = read_file(gi_path)
        print('reset gi.')
    else:
        lines3 = read_file(gi_path2)
        print('update gi.')
    write_file(gi_path3, lines3)


def open_path_dir():
    os.startfile(path)


def open_hero_dir():
    hero_dir = os.path.join(path, "vpk", "pak01_dir", "scripts", "npc", "heroes")
    os.startfile(hero_dir)


def open_bot_dir():
    config = read_config()
    bot_path = config['bot_path']
    os.startfile(bot_path)


def open_dota_path():
    config = read_config()
    dota_path = config['dota_path']
    os.startfile(dota_path)


def open_mod_dir():
    mod_path = os.path.join(read_config()['dota_path'], "game", "mod")
    os.makedirs(mod_path, exist_ok=True)
    os.startfile(mod_path)


def open_skin_dir():
    skin_path = os.path.join(read_config()['dota_path'], "game", "Dota2SkinChanger")
    os.makedirs(skin_path, exist_ok=True)
    os.startfile(skin_path)


def open_skin_dir2():
    skin_path = os.path.join(read_config()['dota_path'], "game", "Dota2SkinChanger2")
    os.makedirs(skin_path, exist_ok=True)
    os.startfile(skin_path)

def open_skin_dir3():
    skin_path = os.path.join(read_config()['dota_path'], "game", "Dota2SkinChanger3")
    os.makedirs(skin_path, exist_ok=True)
    os.startfile(skin_path)


def clean_all_skin():
    skin_file = os.path.join(read_config()['dota_path'], "game", "Dota2SkinChanger", "pak01_dir.vpk")
    skin_file2 = os.path.join(read_config()['dota_path'], "game", "Dota2SkinChanger2", "pak01_dir.vpk")
    skin_file3 = os.path.join(read_config()['dota_path'], "game", "Dota2SkinChanger3", "pak01_dir.vpk")
    if os.path.exists(skin_file): os.remove(skin_file)
    if os.path.exists(skin_file2): os.remove(skin_file2)
    if os.path.exists(skin_file2): os.remove(skin_file3)


def open_general_lua():
    dota_path = read_config()['dota_path']
    lua_path = os.path.join(dota_path, "game", "dota", "scripts", "vscripts", "game", "Customize", "general.lua")
    os.startfile(lua_path)


def open_on_entity_killed_lua():
    bot_path = read_config()['bot_path']
    lua_path = os.path.join(bot_path, "FretBots", "OnEntityKilled.lua")
    os.startfile(lua_path)

def open_gi():
    gi_path = os.path.join(read_config()['dota_path'], "game", "dota", "gameinfo_branchspecific.gi")
    os.startfile(gi_path)

def open_vpk():
    vpk_path = os.path.join(read_config()['dota_path'], "game", "dota", "pak01_dir.vpk")
    os.startfile(vpk_path)

if __name__ == '__main__':
    # copy_steam_cmd()
    # update_gi()
    # update_xp_gold()
    # update_neutral_items()
    # update_items()
    # generate_vpk()
    # copy_bot_cmd()
    # open_bot_dir()
    # open_dota_path()
    # open_general_lua()
    # open_on_entity_killed_lua()
    # clean_all_skin()
    # open_gi()
    open_vpk()
