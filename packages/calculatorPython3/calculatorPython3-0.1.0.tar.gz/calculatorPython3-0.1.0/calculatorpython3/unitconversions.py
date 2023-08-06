class UnitConversions:
    INCH_TO_CM = 2.54
    FEET_TO_METERS = 0.3048
    POUNDS_TO_KILOGRAMS = 0.453592
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
    MILES_TO_KILOMETERS = 1.60934
    GALLONS_TO_LITERS = 3.78541
    OUNCES_TO_MILLILITERS = 29.5735

    @staticmethod
    def inch_to_cm(inches):
        """Convert inches to centimeters."""
        return inches * UnitConversions.INCH_TO_CM

    @staticmethod
    def cm_to_inch(cm):
        """Convert centimeters to inches."""
        return cm / UnitConversions.INCH_TO_CM

    @staticmethod
    def feet_to_meters(feet):
        """Convert feet to meters."""
        return feet * UnitConversions.FEET_TO_METERS

    @staticmethod
    def meters_to_feet(meters):
        """Convert meters to feet."""
        return meters / UnitConversions.FEET_TO_METERS

    @staticmethod
    def pounds_to_kilograms(pounds):
        """Convert pounds to kilograms."""
        return pounds * UnitConversions.POUNDS_TO_KILOGRAMS

    @staticmethod
    def kilograms_to_pounds(kilograms):
        """Convert kilograms to pounds."""
        return kilograms / UnitConversions.POUNDS_TO_KILOGRAMS

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * UnitConversions.FAHRENHEIT_TO_CELSIUS_FACTOR

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def miles_to_kilometers(miles):
        """Convert miles to kilometers."""
        return miles * UnitConversions.MILES_TO_KILOMETERS

    @staticmethod
    def kilometers_to_miles(kilometers):
        """Convert kilometers to miles."""
        return kilometers / UnitConversions.MILES_TO_KILOMETERS

    @staticmethod
    def gallons_to_liters(gallons):
        """Convert gallons to liters."""
        return gallons * UnitConversions.GALLONS_TO_LITERS

    @staticmethod
    def liters_to_gallons(liters):
        """Convert liters to gallons."""
        return liters / UnitConversions.GALLONS_TO_LITERS

    @staticmethod
    def ounces_to_milliliters(ounces):
        """Convert ounces to milliliters."""
        return ounces * UnitConversions.OUNCES_TO_MILLILITERS

    @staticmethod
    def milliliters_to_ounces(milliliters):
        """Convert milliliters to ounces."""
        return milliliters / UnitConversions.OUNCES_TO_MILLILITERS
