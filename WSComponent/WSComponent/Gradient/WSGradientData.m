//
//  WSGradientData.m
//  WSComponent
//
//  Created by Quốc Tuyến on 11/25/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "WSGradientData.h"
#import "NSArray+Extension.h"

@implementation WSGradientData

- (instancetype)initWithColors:(NSArray<UIColor *> *)colors
                    startPoint:(CGPoint)startPoint
                      endPoint:(CGPoint)endPoint {
    self = [super init];
    if (self) {
        _colors = [colors map:^id _Nonnull(UIColor* _Nonnull color) {
            return (__bridge id)color.CGColor;
        }];
        _startPoint = startPoint;
        _endPoint = endPoint;
    }
    return self;
}

@end
