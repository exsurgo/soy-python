import java.util.*;
import com.google.common.collect.ImmutableSet;
import com.google.template.soy.pysrc.restricted.SoyPySrcFunction;
import com.google.template.soy.pysrc.restricted.PyExpr;

/**
 * Provides a function for returning string "Foo Bar".
 */
public class FooBarFunction implements SoyPySrcFunction {

    public PyExpr computeForPySrc(List<PyExpr> params) {
        return new PyExpr("\"Foo Bar\"", Integer.MAX_VALUE);
    }

    public String getName() {
        return "fooBar";
    }

    public Set<Integer> getValidArgsSizes() {
        return ImmutableSet.of(0);
    }

}
