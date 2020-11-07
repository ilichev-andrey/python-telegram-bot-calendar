from enum import Enum


class Locales(Enum):
    ENGLISH = 'en'
    SPANISH = 'eo'
    RUSSIAN = 'ru'


MONTHS = {
    Locales.ENGLISH: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    Locales.SPANISH: ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aŭg", "Sep", "Okt", "Nov", "Dec"],
    Locales.RUSSIAN: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"],
}

DAYS_OF_WEEK = {
    Locales.ENGLISH: ["Mn", "Ts", "Wd", "Th", "Fr", "St", "Sn"],
    Locales.SPANISH: ["L", "M", "M", "Ĵ", "V", "S", "D"],
    Locales.RUSSIAN: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
}