//
//  WSButton.m
//  WSComponent
//
//  Created by Quốc Tuyến on 11/23/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "WSButton.h"

@interface WSButton ()
@property(nonatomic, assign) CGSize currentSize;

@end


@implementation WSButton

- (instancetype)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        _gradientBackgroundColor = [[CAGradientLayer alloc] init];
    }
    return self;
}

- (void)setGradientBackgroundColor:(WSGradientData *)gradientBackgroundColor {
    if (gradientBackgroundColor && gradientBackgroundColor != _gradientBackgroundColor) {
        _gradientBackgroundColor = gradientBackgroundColor;
        CAGradientLayer *layer = [[CAGradientLayer alloc] init];
        layer.startPoint = gradientBackgroundColor.startPoint;
        layer.endPoint = gradientBackgroundColor.endPoint;
        layer.colors = gradientBackgroundColor.colors;
        
        UIGraphicsBeginImageContextWithOptions(layer.frame.size, NO, 0);
        [layer renderInContext:UIGraphicsGetCurrentContext()];
        UIImage *backgroundImage = UIGraphicsGetImageFromCurrentImageContext();
        UIGraphicsEndImageContext();
        
        [self setBackgroundImage:backgroundImage forState:UIControlStateNormal];
    }
}

- (void)layoutSubviews {
    [super layoutSubviews];
    if (!CGSizeEqualToSize(self.currentSize, self.bounds.size)) {
        self.currentSize = self.bounds.size;
        self.layer.cornerRadius = self.currentSize.height / 2;
    }
}

@end
