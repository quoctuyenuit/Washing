//
//  ColorPalettes.m
//  Washing
//
//  Created by Quốc Tuyến on 12/2/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "WSColorPalettes.h"
#import <UIKit/UIKit.h>
#import "NSDictionary+Extension.h"
#import "WSMacros.h"

@interface WSColorPalettes ()

@property(nonatomic, strong) NSDictionary<NSString *, UIColor *> *colorPalettes;

@end

@implementation WSColorPalettes

- (instancetype)initWithJsonified:(NSString *)jsonifiedString {
    NSDictionary *dictionary = [NSDictionary dictionaryWithJsonifiedString:jsonifiedString];
    NSAssert(isValidClass(dictionary, NSDictionary), @"Invalid jsonified string, the string cannot convert to dictionary");
    self = [super init];
    if (self && isValidClass(dictionary, NSDictionary)) {
        NSMutableDictionary<NSString *, UIColor *> *palettes = [NSMutableDictionary dictionary];
        
        for (NSString *colorName in dictionary) {
            NSString *rawValue = [dictionary objectForKey:colorName];
            UIColor *color = [self colorFromString:rawValue];
            
            NSAssert(isValidClass(color, UIColor), @"Cannot parse '%@' with value '%@'", colorName, rawValue);
            [palettes setObject:color forKey:colorName];
        }
        self.colorPalettes = [NSDictionary dictionaryWithDictionary:palettes];
        
    }
    return self;
}

- (UIColor *)colorWithKey:(NSString *)key {
    UIColor *color = [self.colorPalettes objectForKey:key];
    NSAssert(color != nil, @"The key \"%@\" not exists in color palettes", key);
    return color ? : UIColor.clearColor;
}

- (UIColor *)colorFromString:(NSString *)string {
    UIColor *color = nil;
    
    if (string && [string isKindOfClass:[NSString class]]) {
        NSArray<NSString *> *colorComponents = [string componentsSeparatedByString:@","];
        NSInteger numberOfComponents = colorComponents.count;
        
        // HEX color.
        if (numberOfComponents == 1 || numberOfComponents == 2) {
            NSString *hexColor = colorComponents[0];
            
            if (hexColor.length == 7 && [hexColor hasPrefix:@"#"]) {
                NSUInteger r = [self intFromHex:[hexColor substringWithRange:NSMakeRange(1, 2)]];
                NSUInteger g = [self intFromHex:[hexColor substringWithRange:NSMakeRange(3, 2)]];
                NSUInteger b = [self intFromHex:[hexColor substringWithRange:NSMakeRange(5, 2)]];
                CGFloat a = (numberOfComponents == 2) ? [colorComponents[1] floatValue] : 1;
                
                color = [UIColor colorWithRed:r/255.0 green:g/255.0 blue:b/255.0 alpha:a];
            }
        }
        // RGB color
        else if (numberOfComponents == 3) {
            CGFloat r = [colorComponents[0] floatValue];
            CGFloat g = [colorComponents[1] floatValue];
            CGFloat b = [colorComponents[2] floatValue];
            
            color = [UIColor colorWithRed:r/255.0 green:g/255.0 blue:b/255.0 alpha:1];
        }
        // RGBA color
        else if (numberOfComponents == 4) {
            CGFloat r = [colorComponents[0] floatValue];
            CGFloat g = [colorComponents[1] floatValue];
            CGFloat b = [colorComponents[2] floatValue];
            CGFloat a = [colorComponents[3] floatValue];
            
            color = [UIColor colorWithRed:r/255.0 green:g/255.0 blue:b/255.0 alpha:a];
        }
    }
    
    return color;
}

- (unsigned int)intFromHex:(NSString *)hex {
    unsigned int result = 0;
    
    if (hex && [hex isKindOfClass:[NSString class]]) {
        NSScanner *scanner = [NSScanner scannerWithString:hex];
        [scanner scanHexInt:&result];
    }
    
    return result;
}

@end
