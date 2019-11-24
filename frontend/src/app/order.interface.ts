export interface Order {
    id: number;
    computer_id: number;
    user_id: number;
  }

  export interface Computer {
    id: number;
    processor_id: number;
    motherboard_id: number;
    memory_id: Memory[];
    graphic_card_id: number;
  }

  export interface Processor {
    id: number;
    processor_description: string;
    processor_brand: string;
  }

  export interface MotherBoard {
    id: number;
    motherboard_description: string;
    supported_processors: string;
    slots_ram: number;
    max_ram_supported: number;
    integrated_graphic: boolean;
  }

  export interface Memory {
    id: number;
    ram_description: string;
    ram_size: number;
  }

  export interface GraphicCard {
    graphic_card_description: string;
  }

  export interface User {
    id: number;
    username: string;
  }