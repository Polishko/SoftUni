from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        if power_hardware not in System._hardware:
            System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        if heavy_hardware not in System._hardware:
            System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]

        if not searched_hardware:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        searched_hardware[0].install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]

        if not searched_hardware:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        searched_hardware[0].install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]
        searched_software = [s for s in System._software if s.name == software_name]

        if searched_hardware and searched_software:
            searched_hardware[0].uninstall(searched_software[0])
            System._software.remove(searched_software[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_soft_memory = sum([s.memory_consumption for s in System._software])
        total_hard_memory = sum([h.memory for h in System._hardware])
        total_soft_capacity = sum([s.capacity_consumption for s in System._software])
        total_hard_capacity = sum([h.capacity for h in System._hardware])

        result = f"System Analysis\n" \
                 + f"Hardware Components: {len(System._hardware)}\n" \
                 + f"Software Components: {len(System._software)}\n" \
                 + f"Total Operational Memory: {total_soft_memory} / {total_hard_memory}\n"\
                 + f"Total Capacity Taken: {total_soft_capacity} / {total_hard_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ""

        for h in System._hardware:
            soft_components = ", ".join([s.name for s in h.software_components]) if len(h.software_components) != 0 else "None"

            info_h = f"Hardware Component - {h.name}\n" \
                     + f"Express Software Components: " \
                       f"{len([s for s in h.software_components if s.software_type == 'Express'])}\n" \
                     + f"Light Software Components: " \
                       f"{len([s for s in h.software_components if s.software_type == 'Light'])}\n" \
                     + f"Memory Usage: {sum(s.memory_consumption for s in h.software_components)} / {h.memory}\n" \
                     + f"Capacity Usage: {sum(s.capacity_consumption for s in h.software_components)} / {h.capacity}\n" \
                     + f"Type: {h.hardware_type}\n" \
                     + f"Software Components: {soft_components}\n"

            result += info_h

        return result
