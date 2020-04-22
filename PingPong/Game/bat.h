#include <SFML/Graphics.hpp>
using namespace sf;
class Bat{
private:
    Vector2f position;
    RectangleShape batShape;
    float speedBat = .3f;
public:
    Bat(float starLoctX, float startLocY);
    FloatRect getPosition();
    RectangleShape getShape();
    void moveRight();
    void moveLeft();
    void update();
};