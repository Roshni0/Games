#include <SFML/Graphics.hpp>
using namespace sf;
class Ball{
private:
    Vector2f position;
    RectangleShape ballShape;
    float velocityX = .2f;
    float velocityY = .2f;
public:
    Ball(float startX, float startY);
    FloatRect getPosition();
    RectangleShape getShape();
    float getXVelocity();
    void reboundSides();
    void reboundBatOrTop();
    void hitBottom();
    void update();
};